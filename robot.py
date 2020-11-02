import wpilib
import wpilib.drive
import deadzone

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.left_motor = wpilib.Spark(0)
        self.right_motor = wpilib.Spark(1)
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)
        self.stick = wpilib.Joystick(0)
        self.timer = wpilib.Timer()

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.timer.reset()
        self.timer.start()

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        if self.timer.get() < 2.0:
            print("Driving forward at half speed")
            self.drive.arcadeDrive(-0.5, 0)  # Drive forwards at half speed for 2 seconds
        elif self.timer.get() < 3.0:
            print("Driving at a 45 degree angle at half speed")
            self.drive.arcadeDrive(-0.5, 0.25)  # Drive at a 45 degree angle for 1 second
        elif self.timer.get() < 8.0:
            print("Driving forwards at full speed")
            self.drive.arcadeDrive(-1, 0)  # Drive forwards at full speed for 5 seconds
        else:
            print("Awaiting end of autonomous period")
            self.drive.arcadeDrive(0, 0)  # Stop robot

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""

        #  This is the deadzone code. If there are issues with it, comment it out, and uncomment the code below.
        #  This will activate arcadeDrive without any deadzone code.
        driveDirection = deadzone.addDeadzone(self.stick.getY(), self.stick.getX())
        print("X: " + str(driveDirection["x"]))
        print("Y: " + str(driveDirection["y"]))
        self.drive.arcadeDrive(driveDirection["x"], driveDirection["y"])

        #  Uncomment this to remove deadzone
        # self.drive.arcadeDrive(self.stick.getX(), self.stick.getY())


if __name__ == "__main__":
    wpilib.run(MyRobot)
