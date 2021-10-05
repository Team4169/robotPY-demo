import wpilib
import wpilib.drive
import ctre
import deadzone
from constants import constants

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """

        self.front_left_motor = ctre.WPI_TalonSRX(constants["frontLeftPort"])
        self.rear_left_motor = ctre.WPI_TalonSRX(constants["rearLeftPort"])
        #
        self.front_right_motor = ctre.WPI_TalonSRX(constants["frontRightPort"])
        self.rear_right_motor = ctre.WPI_TalonSRX(constants["rearRightPort"])
        self.drive = wpilib.drive.MecanumDrive(
            self.front_left_motor,
            self.rear_left_motor,
            self.front_right_motor,
            self.rear_right_motor)
        self.front_left_motor.setInverted(True)
        self.rear_left_motor.setInverted(True)
        # self.test_motor = wpilib.PWMTalonSRX(10)
        self.test_motor = ctre.WPI_TalonSRX(10)
        #
        # # self.stick = wpilib.Joystick(0)
        self.controller = wpilib.XboxController(0)
        # self.timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):

        """
        driveCartesian(ySpeed: float, xSpeed: float, zRotation: float, gyroAngle: float = 0.0)

        NOTE: I herd coded zRotation at 0, and I don't full understand what that will do
        """

        """This function is called periodically during autonomous."""
        # if self.timer.get() < 2.0:
        #     print("Driveing diagonal at half speed")
        #     self.drive.driveCartesian(0.5, 0.5, 0)  # Drive diagonal at half speed
        # elif self.timer.get() < 3.0:
        #     print("Driving forward at full speed")
        #     self.drive.driveCartesian(1, 0, 0)  # Drive forward at full speed
        # elif self.timer.get() < 8.0:
        #     print("Driving right at full speed")
        #     self.drive.driveCartesian(0, 1, 0)  # Drive right at full speed
        # else:
        #     print("Awaiting end of autonomous period")
        #     self.drive.driveCartesian(0, 0, 0)  # Stop the robot and await end of autonomous

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""

        #  This is the deadzone code. If there are issues with it, comment it out, and uncomment the code below.
        #  This will activate arcadeDrive without any deadzone code.
        # driveDirection = deadzone.addDeadzone(self.stick.getY(), self.stick.getX())

        # print("X: " + str(driveDirection["x"]))
        # print("Y: " + str(driveDirection["y"]))

        # self.drive.driveCartesian(driveDirection["y"], driveDirection["x"], 0)  # Drive on an X Y plain using joystick axis
        print("The drive X left is: ",self.controller.getX(self.controller.Hand.kLeftHand))
        print("The drive Y left is: ",self.controller.getY(self.controller.Hand.kLeftHand))
        self.drive.driveCartesian(
            self.controller.getX(self.controller.Hand.kLeftHand),
            self.controller.getY(self.controller.Hand.kLeftHand),
            self.controller.getY(self.controller.Hand.kRightHand),0)
        isAPressed = self.controller.getAButton()
        # print(isAPressed)
        isBpressed = self.controller.getBButton()
        print("is b pressed:",isBpressed)
        if isBpressed:
            print("b pressed!")
            self.front_left_motor.set(1)
        else:
            self.front_left_motor.set(0)
        if self.controller.getXButton():
            self.front_right_motor.set(1)
        else:
            self.front_right_motor.set(0)
        if self.controller.getYButton():
            self.rear_left_motor.set(1)
        else:
            self.rear_left_motor.set(0)
        if self.controller.getAButton():
            self.rear_right_motor.set(1)
        else:
            self.rear_right_motor.set(0)
        if isAPressed:
            self.test_motor.set(1)
            # print("Go!")
        else:
            self.test_motor.set(0)
            # print("Stop!")
        # print("!!")
        # print(self.test_motor.getSpeed())
        # print(self.test_motor.get())
        # print("??")

if __name__ == "__main__":
    wpilib.run(MyRobot)
