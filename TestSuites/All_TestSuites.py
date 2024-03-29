# Creating and Running Test Suites | Batch Testing
import unittest
from Package1.TC_LoginTest import LoginTest
from Package1.TC_SignupTest import SignUpTest
from Package2.TC_PaymentTest import PaymentTest
from Package2.TC_PaymentReturnsTest import PaymentReturnsTest

# Get all tests from LogInTest, SignUpTest, PaymentTest, and PaymentReturnsTest
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# Creating Test Suites
sanityTestSuite = unittest.TestSuite([tc1, tc2])  # sanity Test Suite
functionalTestSuite = unittest.TestSuite([tc3, tc4])  # functional Test Suite
# unittest.TextTestRunner().run(sanityTestSuite)
# unittest.TextTestRunner().run(functionalTestSuite)

masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])  # master Test Suite | All Test Cases
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)


