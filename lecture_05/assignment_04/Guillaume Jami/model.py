import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import math as m
import simple_comm as c
import simple_ur_script as ur


class Fabrication():
    ROBOT_IP = "192.168.10.10"

    def __init__(self, fabricate=False, brick_planes=None, robot_ip=ROBOT_IP):
        self.brick_planes = brick_planes
        self.robot_ip = robot_ip
        self.accel = 0.1
        self.vel = 0.1
        self.script = ""
        self.way_planes = []

    def tcp(self):
        self.script += ur.set_tcp_by_angles(
            0.0, 0.0, 74.0, m.radians(0.0), m.radians(180.0), m.radians(0))

    def set_robot_base_plane(self):

        rs.MessageBox(
            "move robot to base plane origin, press OK when there", 0)
        data = c.listen_to_robot(ROBOT_IP)
        pose = data['pose']
        pt_1 = rg.Point3d(pose[0]*1000, pose[1]*1000, pose[2]*1000)
        print(pt_1)
        rs.MessageBox(
            "move robot to base plane positive x direction, press OK when there", 0)
        data = c.listen_to_robot(ROBOT_IP)
        pose = data['pose']
        pt_2 = rg.Point3d(pose[0]*1000, pose[1]*1000, pose[2]*1000)
        print(pt_2)
        rs.MessageBox(
            "move robot to base plane positive y direction, press OK when there", 0)
        data = c.listen_to_robot(robot_ip)
        pose = data['pose']
        pt_3 = rg.Point3d(pose[0]*1000, pose[1]*1000, pose[2]*1000)
        print(pt_3)

        robot_base = rg.Plane(pt_1, pt_2-pt_1, pt_3-pt_1)
        text_file = open("robot_base.txt", "w")
        text_file.write(str(robot_base.Origin)+"," +
                        str(robot_base.XAxis)+","+str(robot_base.YAxis))
        text_file.close()

    # def load_robot_base_plane(self):
        text_file = open("robot_base.txt", "r")
        string = text_file.read()
        values = string.split(",")
        values = [float(value) for value in values]

        base_origin = rg.Point3d(values[0], values[1], values[2])
        base_x_axis = rg.Vector3d(values[3], values[4], values[5])
        base_y_axis = rg.Vector3d(values[6], values[7], values[8])

        base_plane = rg.Plane(base_origin, base_x_axis, base_y_axis)
        return base_plane

    def set_robot_base_plane_from_pts(self):

        pt_0 = rg.Point3d(327, 230, 0)  # base plane origin
        # point on base plane positive x direction
        pt_1 = rg.Point3d(499, 230, 0)
        pt_2 = rg.Point3d(499, 499, 0)  # point on base plane positive xy

        robot_base = rg.Plane(pt_0, pt_1-pt_0, pt_2-pt_0)
        return robot_base

    def rhino_to_robot_space(self, in_plane):
        plane = in_plane.Clone()
        _r_matrix = rg.Transform.PlaneToPlane(
            rg.Plane.WorldXY, self.set_robot_base_plane_from_pts())
        plane.Transform(_r_matrix)
        return plane

    def robot_transformation(self):  # LOAD robot model
        _robot_matrix = rg.Transform.PlaneToPlane(
            self.set_robot_base_plane_from_pts(), rg.Plane.WorldXY)
        return _robot_matrix

    def pickup_brick(self, pick_up_plane):
        """Example of a method's documentation.

        Parameters
        ----------
        point_x : float
        Description of the first param
        point_y : float
        Description of the second param
        """

        safe_distance = 50

        safe_plane = pick_up_plane.Clone()
        safe_plane.Translate(rg.Vector3d(0, 0, safe_distance))

        self.script += ur.move_l(safe_plane, self.accel, self.vel)
        self.way_planes.append(safe_plane)

        self.script += ur.move_l(pick_up_plane, self.accel, self.vel)
        self.way_planes.append(pick_up_plane)

        self.script += ur.set_digital_out(4, True)
        self.script += ur.sleep(1)

        self.script += ur.move_l(safe_plane, self.accel, self.vel)
        self.way_planes.append(safe_plane)

        return None

    def place_brick(self, plane):
        """
        this function gereates the robotic sequience for placing a brick
        Requires a plane wich describes the possition of the brick"""

        safe_distance = 50

        safe_plane = plane.Clone()
        safe_plane.Translate(rg.Vector3d(0, 0, safe_distance))

        self.script += ur.move_l(safe_plane, self.accel, self.vel)
        self.way_planes.append(safe_plane)

        self.script += ur.move_l(plane, self.accel, self.vel)
        self.way_planes.append(plane)

        self.script += ur.set_digital_out(4, False)
        self.script += ur.sleep(1)

        self.script += ur.move_l(safe_plane, self.accel, self.vel)
        self.way_planes.append(safe_plane)

        return None

    def procedure(self, transform=True):

        self.tcp()
        robot_planes = []

        if transform:
            pick_up_plane = rg.Plane(rg.Point3d(
                0, 450, 0), rg.Vector3d.XAxis, rg.Vector3d.YAxis)
            for plane in (self.brick_planes):
                robot_planes.append(self.rhino_to_robot_space(plane))

        else:
            pick_up_plane = self.rhino_to_robot_space(
            rg.Plane(rg.Point3d(0, 450, 0), rg.Vector3d.XAxis, rg.Vector3d.YAxis))
            robot_planes = self.brick_planes

            for plane in (robot_planes):
                self.pickup_brick(pick_up_plane)
                self.place_brick(plane)

    def visualize(self):
        """this funktion visualizes the planes wich are sent to the robot"""

        crv = []

        for plane in self.way_planes:
            #print (plane.Origin)
            pt = plane.Origin
            crv.append(pt)

        curve = rg.NurbsCurve.Create(False, 1, crv)
        print(curve)
        return self.way_planes, curve

    def send(self):
        """
        this funktion sends the script to the robot."""

        self.script = c.concatenate_script(self.script)
        #c.send_script(self.script, self.robot_ip)
        return self.script


class Brick(object):
    REFERENCE_LENGTH = 31
    REFERENCE_WIDTH = 25
    REFERENCE_HEIGHT = 8

    def __init__(self, plane, length=REFERENCE_LENGTH, width=REFERENCE_WIDTH, height=REFERENCE_HEIGHT):
        """Brick containes picking plane, placing plane and geometry

        Parameters
        ----------
        plane : Rhino Geometry plane
        this plane describes the possition and orientation of the Brick

        """
        self.plane = plane
        self.length = length
        self.width = width
        self.height = height


    def dimensions(self):
        """returns the dimenesnions of the brick:

        Returns
        ----------
        [length : float, width : float, height: float]

        """

        return self.length, self.width, self.height

    def pts(self):
        """returns 8 points describing the brick:

        Returns
        ----------
        [pt0 : bottom point at origin,
        pt1 : bottom point at possitive Y,
        pt2 : bottom point at possitive X,
        pt3 : bottom point at possitive X and poossitive Y,
        pt4 : top point at origin,
        pt1 : top point at possitive Y,
        pt2 : top point at possitive X,
        pt3 : top point at possitive X and poossitive Y]

        """

        pt_0 = rg.Point3d(0, 0, 0)
        pt_1 = rg.Point3d(self.length, 0, 0)
        pt_2 = rg.Point3d(self.length, self.width, 0)
        pt_3 = rg.Point3d(0, self.width, 0)

        pt_4 = rg.Point3d(0, 0, self.height)
        pt_5 = rg.Point3d(self.length, 0, self.height)
        pt_6 = rg.Point3d(self.length, self.width, self.height)
        pt_7 = rg.Point3d(0, self.width, self.height)

        b_pts = [pt_0, pt_1, pt_2, pt_3, pt_4, pt_5, pt_6, pt_7]

        return b_pts

    def origin(self):
        """returns the origin plane in the centre of the base of the brick:

        Returns
        ----------
        [Rhino Geometry Plane]

        """
        vec = (self.pts()[2]-self.pts()[0])/2
        origin = self.pts()[0] + vec
        plane = rg.Plane(origin, rg.Vector3d.XAxis, rg.Vector3d.YAxis)
        return plane

    def transformation(self):
        """Transoformation matrix fot transformating the brick to the brick possiotn:

        Returns
        ----------
        [Rhino Geometry Transformation]

        """
        return rg.Transform.PlaneToPlane(self.origin(), self.plane)

    def base_plane(self):
        """Base plane of the transformed brick:

        Returns
        ----------
        [Rhino Geometry Plane]

        """

        p_plane = self.origin()
        p_plane.Transform(self.transformation())
        return p_plane

    def picking_plane(self):
        """Robot's picking plane on the transformed brick:

        Returns
        ----------
        [Rhino Geometry Plane]

        """
        p_plane = self.origin()
        p_pt = p_plane.Origin
        p_plane = rg.Plane(p_pt+rg.Vector3d(0, 0, self.height),
                           p_plane.XAxis, p_plane.YAxis)

        p_plane.Transform(self.transformation())
        return p_plane

    def surface(self):
        """NURB surfaces depicting the brick:

        Returns
        ----------
        [srf0 : base surface,
        srf1 : long edge,
        srf2 : top surface
        srf3 : long edge,
        srf4 : short edge
        srf5 : short edge]

        """
        tran_brick_pts = []
        for pt in self.pts():
            transformation_pt = pt.Clone()
            transformation_pt.Transform(self.transformation())
            tran_brick_pts.append(transformation_pt)

        pt_0, pt_1, pt_2, pt_3, pt_4, pt_5, pt_6, pt_7 = tran_brick_pts

        srf_0 = rg.NurbsSurface.CreateFromPoints(
            [pt_0, pt_1, pt_3, pt_2], 2, 2, 1, 1)
        srf_1 = rg.NurbsSurface.CreateFromPoints(
            [pt_0, pt_1, pt_4, pt_5], 2, 2, 1, 1)
        srf_2 = rg.NurbsSurface.CreateFromPoints(
            [pt_4, pt_5, pt_7, pt_6], 2, 2, 1, 1)
        srf_3 = rg.NurbsSurface.CreateFromPoints(
            [pt_6, pt_7, pt_2, pt_3], 2, 2, 1, 1)
        srf_4 = rg.NurbsSurface.CreateFromPoints(
            [pt_0, pt_3, pt_4, pt_7], 2, 2, 1, 1)
        srf_5 = rg.NurbsSurface.CreateFromPoints(
            [pt_1, pt_2, pt_5, pt_6], 2, 2, 1, 1)

        return (srf_0, srf_1, srf_2, srf_3, srf_4, srf_5)

    def mesh(self):
        """Mesh  depicting the brick:

        Returns
        ----------
        mesh_brick : Mesh
        """

        mesh_brick = rg.Mesh.CreateFromBox(self.pts(), 1, 1, 1)
        mesh_brick.Transform(self.transformation())

        return mesh_brick


class Wall():
    def __init__(self, x_cnt, z_cnt):
        """Wall generates and contains the bricks

        Parameters
        ----------
        x_cnt : int
        this number corresponds to the length of the wall (amount of bricks)

        x_cnt : int
        this number corresponds to the hight of the wall
        (amount of brick layers)

        """

        self.x_cnt = x_cnt
        self.z_cnt = z_cnt


        self.b_length = Brick.REFERENCE_LENGTH
        self.b_width = Brick.REFERENCE_WIDTH
        self.b_height = Brick.REFERENCE_HEIGHT

    def brick_possitions(self):
        """Genrates a Rhino Geometry plane for each brick

        This is where the design of the wall is created.

        Returns
        ----------
        brick_planes : [Rhino Geometry Plane, Rhino Geometry Plane, ...]

        """

        brick_planes = []
        for i in range(self.z_cnt):  # layer count
            for j in range(self.x_cnt):  # layer length

                if i % 2 == 0:
                    x_pos = j * (self.b_length+1)
                    rotation = m.radians(10)
                else:
                    x_pos = j * (self.b_length+1) + (self.b_length/2)-1
                    rotation = m.radians(-10)

                z_pos = i * (self.b_height)

                origin = rg.Point3d(x_pos, 0, z_pos)
                plane = rg.Plane(origin, rg.Vector3d.XAxis, rg.Vector3d.YAxis)
                plane.Rotate(rotation, rg.Vector3d.ZAxis)
                brick_planes.append(plane)

        return brick_planes

    def geometric_model(self):
        """Generates a 3D model of the wall

        Returns
        ----------
        geo : [Rhino Geometry Surface, Rhino Geometry Surface, ...]

        """

        planes = []
        geo = []

        for plane in self.brick_possitions():
            myBrick = Brick(plane)
            planes.append(myBrick.base_plane())
            # geo.extend(myBrick.surface())

            geo.append(myBrick.mesh())

        visualizeFabrication = Fabrication(
            brick_planes=self.brick_possitions())
        visualizeFabrication.procedure(transform=False)
        robot_matrix = visualizeFabrication.robot_transformation()

        print(robot_matrix)

        return geo, visualizeFabrication.visualize(), robot_matrix

    def fabrication_model(self):
        """Generates all the data necessary for the robotic fabrication
        process and sends the comands to the robot

        Returns script
        ----------
        script : "UR script"
        """

        myFabrication = Fabrication(brick_planes=self.brick_possitions())

        myFabrication.procedure()
        script = myFabrication.send()

        return script, myFabrication.visualize()
