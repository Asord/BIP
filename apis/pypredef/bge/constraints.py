'''This is the Python API for the Physics Constraints'''

ANGULAR_CONSTRAINT = int
CONETWIST_CONSTRAINT = int
DBG_DISABLEBULLETLCP = int
DBG_DRAWAABB = int
DBG_DRAWCONSTRAINTLIMITS = int
DBG_DRAWCONSTRAINTS = int
DBG_DRAWCONTACTPOINTS = int
DBG_DRAWFREATURESTEXT = int
DBG_DRAWTEXT = int
DBG_DRAWWIREFRAME = int
DBG_ENABLECCD = int
DBG_ENABLESATCOMPARISION = int
DBG_FASTWIREFRAME = int
DBG_NODEBUG = int
DBG_NOHELPTEXT = int
DBG_PROFILETIMINGS = int
GENERIC_6DOF_CONSTRAINT = int
LINEHINGE_CONSTRAINT = int
POINTTOPOINT_CONSTRAINT = int
VEHICLE_CONSTRAINT = int
def createConstraint(*argv):
	'''createConstraint(ob1,ob2,float restLength,float restitution,float damping)'''

error = str
def exportBulletFile(*argv):
	'''export a .bullet file'''

def getAppliedImpulse(*argv):
	'''getAppliedImpulse(int constraintId)'''

def getCharacter(*argv):
	'''getCharacter(KX_GameObject obj)'''

def getVehicleConstraint(*argv):
	'''getVehicleConstraint(int constraintId)'''

def removeConstraint(*argv):
	'''removeConstraint(int constraintId)'''

def setCcdMode(*argv):
	'''setCcdMode(int ccdMode)
Very experimental, not recommended'''

def setContactBreakingTreshold(*argv):
	'''setContactBreakingTreshold(float breakingTreshold)
Reasonable default is 0.02 (if units are meters)'''

def setDeactivationAngularTreshold(*argv):
	'''setDeactivationAngularTreshold(float angularTreshold)'''

def setDeactivationLinearTreshold(*argv):
	'''setDeactivationLinearTreshold(float linearTreshold)'''

def setDeactivationTime(*argv):
	'''setDeactivationTime(float time)
This sets the time after which a resting rigidbody gets deactived'''

def setDebugMode(*argv):
	'''setDebugMode(int mode)'''

def setGravity(*argv):
	'''setGravity(float x,float y,float z)'''

def setLinearAirDamping(*argv):
	'''setLinearAirDamping(float damping)
Very experimental, not recommended'''

def setNumIterations(*argv):
	'''setNumIterations(int numiter)
This sets the number of iterations for an iterative constraint solver'''

def setNumTimeSubSteps(*argv):
	'''setNumTimeSubSteps(int numsubstep)
This sets the number of substeps for each physics proceed. Tradeoff quality for performance.'''

def setSolverDamping(*argv):
	'''setDamping(float damping)
Very experimental, not recommended'''

def setSolverTau(*argv):
	'''setTau(float tau)
Very experimental, not recommended'''

def setSolverType(*argv):
	'''setSolverType(int solverType)
Very experimental, not recommended'''

def setSorConstant(*argv):
	'''setSorConstant(float sor)
Very experimental, not recommended'''

def setUseEpa(*argv):
	'''setUseEpa(int epa)
Very experimental, not recommended'''


