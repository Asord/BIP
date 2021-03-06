"""This module provides access to the game engine data types."""

getset_descriptor = None

class BL_ActionActuator:
	action = getset_descriptor
	blendIn = getset_descriptor
	blendTime = getset_descriptor
	channelNames = getset_descriptor
	executePriority = getset_descriptor
	frame = getset_descriptor
	frameEnd = getset_descriptor
	framePropName = getset_descriptor
	frameStart = getset_descriptor
	def getChannel(*argv):
		pass

	invalid = getset_descriptor
	layer = getset_descriptor
	layerWeight = getset_descriptor
	mode = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	priority = getset_descriptor
	propName = getset_descriptor
	def setChannel(*argv):
		"""setChannel(channel, matrix)
- channel   : A string specifying the name of the bone channel.
- matrix    : A 4x4 matrix specifying the overriding transformation
              as an offset from the bone's rest position."""

	useContinue = getset_descriptor

class BL_ArmatureActuator:
	constraint = getset_descriptor
	executePriority = getset_descriptor
	influence = getset_descriptor
	invalid = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	subtarget = getset_descriptor
	target = getset_descriptor
	type = getset_descriptor
	weight = getset_descriptor

class BL_ArmatureBone:
	arm_head = getset_descriptor
	arm_mat = getset_descriptor
	arm_tail = getset_descriptor
	bbone_segments = getset_descriptor
	bone_mat = getset_descriptor
	children = getset_descriptor
	connected = getset_descriptor
	head = getset_descriptor
	hinge = getset_descriptor
	inherit_scale = getset_descriptor
	invalid = getset_descriptor
	length = getset_descriptor
	name = getset_descriptor
	parent = getset_descriptor
	roll = getset_descriptor
	tail = getset_descriptor

class BL_ArmatureChannel:
	bone = getset_descriptor
	channel_matrix = getset_descriptor
	has_ik = getset_descriptor
	ik_dof_x = getset_descriptor
	ik_dof_y = getset_descriptor
	ik_dof_z = getset_descriptor
	ik_limit_x = getset_descriptor
	ik_limit_y = getset_descriptor
	ik_limit_z = getset_descriptor
	ik_lin_control = getset_descriptor
	ik_lin_weight = getset_descriptor
	ik_max_x = getset_descriptor
	ik_max_y = getset_descriptor
	ik_max_z = getset_descriptor
	ik_min_x = getset_descriptor
	ik_min_y = getset_descriptor
	ik_min_z = getset_descriptor
	ik_rot_control = getset_descriptor
	ik_rot_weight = getset_descriptor
	ik_stiffness_x = getset_descriptor
	ik_stiffness_y = getset_descriptor
	ik_stiffness_z = getset_descriptor
	ik_stretch = getset_descriptor
	invalid = getset_descriptor
	joint_rotation = getset_descriptor
	location = getset_descriptor
	name = getset_descriptor
	parent = getset_descriptor
	pose_head = getset_descriptor
	pose_matrix = getset_descriptor
	pose_tail = getset_descriptor
	rotation_euler = getset_descriptor
	rotation_mode = getset_descriptor
	rotation_quaternion = getset_descriptor
	scale = getset_descriptor

class BL_ArmatureConstraint:
	active = getset_descriptor
	enforce = getset_descriptor
	headtail = getset_descriptor
	ik_dist = getset_descriptor
	ik_flag = getset_descriptor
	ik_mode = getset_descriptor
	ik_type = getset_descriptor
	ik_weight = getset_descriptor
	invalid = getset_descriptor
	lin_error = getset_descriptor
	name = getset_descriptor
	rot_error = getset_descriptor
	subtarget = getset_descriptor
	target = getset_descriptor
	type = getset_descriptor

class BL_ArmatureObject:
	actuators = getset_descriptor
	def addDebugProperty(*argv):
		"""addDebugProperty(name, visible=1)
Added or remove a debug property to the debug list."""

	def alignAxisToVect(*argv):
		pass

	angularDamping = getset_descriptor
	angularVelocity = getset_descriptor
	angularVelocityMax = getset_descriptor
	angularVelocityMin = getset_descriptor
	def applyForce(*argv):
		pass

	def applyImpulse(*argv):
		pass

	def applyMovement(*argv):
		pass

	def applyRotation(*argv):
		pass

	def applyTorque(*argv):
		pass

	attrDict = getset_descriptor
	channels = getset_descriptor
	children = getset_descriptor
	childrenRecursive = getset_descriptor
	collisionCallbacks = getset_descriptor
	collisionGroup = getset_descriptor
	collisionMask = getset_descriptor
	color = getset_descriptor
	components = getset_descriptor
	constraints = getset_descriptor
	controllers = getset_descriptor
	culled = getset_descriptor
	cullingBox = getset_descriptor
	currentLodLevel = getset_descriptor
	debug = getset_descriptor
	debugRecursive = getset_descriptor
	def disableRigidBody(*argv):
		pass

	def draw(*argv):
		"""Draw Debug Armature"""

	def enableRigidBody(*argv):
		pass

	def endObject(*argv):
		pass

	def get(*argv):
		pass

	def getActionFrame(*argv):
		"""getActionFrame(layer=0)
Gets the current frame of the action playing in the supplied layer"""

	def getActionName(*argv):
		"""getActionName(layer=0)
Gets the name of the current action playing in the supplied layer"""

	def getAngularVelocity(*argv):
		pass

	def getAxisVect(*argv):
		pass

	def getDistanceTo(*argv):
		"""getDistanceTo(other): get distance to another point/KX_GameObject"""

	def getLinearVelocity(*argv):
		pass

	def getPhysicsId(*argv):
		pass

	def getPropertyNames(*argv):
		pass

	def getReactionForce(*argv):
		pass

	def getVectTo(*argv):
		"""getVectTo(other): get vector and the distance to another point/KX_GameObject
Returns a 3-tuple with (distance,worldVector,localVector)"""

	def getVelocity(*argv):
		pass

	groupMembers = getset_descriptor
	groupObject = getset_descriptor
	invalid = getset_descriptor
	def isPlayingAction(*argv):
		"""isPlayingAction(layer=0)
Checks to see if there is an action playing in the given layer"""

	isSuspendDynamics = getset_descriptor
	life = getset_descriptor
	linVelocityMax = getset_descriptor
	linVelocityMin = getset_descriptor
	linearDamping = getset_descriptor
	linearVelocity = getset_descriptor
	localAngularVelocity = getset_descriptor
	localInertia = getset_descriptor
	localLinearVelocity = getset_descriptor
	localOrientation = getset_descriptor
	localPosition = getset_descriptor
	localScale = getset_descriptor
	localTransform = getset_descriptor
	lodManager = getset_descriptor
	mass = getset_descriptor
	meshes = getset_descriptor
	name = getset_descriptor
	occlusion = getset_descriptor
	orientation = getset_descriptor
	parent = getset_descriptor
	def playAction(*argv):
		"""playAction(name, start_frame, end_frame, layer=0, priority=0 blendin=0, play_mode=ACT_MODE_PLAY, layer_weight=0.0, ipo_flags=0, speed=1.0)
Plays an action"""

	position = getset_descriptor
	def rayCast(*argv):
		"""rayCast(to,from,dist,prop,face,xray,poly,mask): cast a ray and return 3-tuple (object,hit,normal) or 4-tuple (object,hit,normal,polygon) or 4-tuple (object,hit,normal,polygon,hituv) of contact point with object within dist that matches prop.
 If no hit, return (None,None,None) or (None,None,None,None) or (None,None,None,None,None).
 to   = 3-tuple or object reference for destination of ray (if object, use center of object)
 from = 3-tuple or object reference for origin of ray (if object, use center of object)
        Can be None or omitted => start from self object center
 dist = max distance to look (can be negative => look behind); 0 or omitted => detect up to to
 prop = property name that object must have; can be omitted => detect any object
 face = normal option: 1=>return face normal; 0 or omitted => normal is oriented towards origin
 xray = X-ray option: 1=>skip objects that don't match prop; 0 or omitted => stop on first object
 poly = polygon option: 1=>return value is a 4-tuple and the 4th element is a KX_PolyProxy object
                           which can be None if hit object has no mesh or if there is no hit
                        2=>return value is a 5-tuple, the 4th element is the KX_PolyProxy object
                           and the 5th element is the vector of UV coordinates at the hit point of the None if there is no UV mapping
        If 0 or omitted, return value is a 3-tuple
 mask = collision mask: the collision mask that ray can hit, 0 < mask < 65536
Note: The object on which you call this method matters: the ray will ignore it.
      prop and xray option interact as follow:
        prop off, xray off: return closest hit or no hit if there is no object on the full extend of the ray
        prop off, xray on : idem
        prop on,  xray off: return closest hit if it matches prop, no hit otherwise
        prop on,  xray on : return closest hit matching prop or no hit if there is no object matching prop on the full extend of the ray"""

	def rayCastTo(*argv):
		"""rayCastTo(other,dist,prop): look towards another point/KX_GameObject and return first object hit within dist that matches prop
prop = property name that object must have; can be omitted => detect any object
dist = max distance to look (can be negative => look behind); 0 or omitted => detect up to other
other = 3-tuple or object reference"""

	def reinstancePhysicsMesh(*argv):
		pass

	def removeParent(*argv):
		pass

	def replaceMesh(*argv):
		pass

	def replacePhysicsShape(*argv):
		pass

	def restoreDynamics(*argv):
		pass

	def restorePhysics(*argv):
		pass

	scaling = getset_descriptor
	scene = getset_descriptor
	def sendMessage(*argv):
		"""sendMessage(subject, [body, to])
sends a message in same manner as a message actuatorsubject = Subject of the message (string)body = Message body (string)to = Name of object to send the message to"""

	sensors = getset_descriptor
	def setActionFrame(*argv):
		"""setActionFrame(frame, layer=0)
Set the current frame of the action playing in the supplied layer"""

	def setAngularVelocity(*argv):
		pass

	def setCollisionMargin(*argv):
		pass

	def setDamping(*argv):
		pass

	def setLinearVelocity(*argv):
		pass

	def setOcclusion(*argv):
		pass

	def setParent(*argv):
		pass

	def setVisible(*argv):
		pass

	state = getset_descriptor
	def stopAction(*argv):
		"""stopAction(layer=0)
Stop playing the action on the given layer"""

	def suspendDynamics(*argv):
		pass

	def suspendPhysics(*argv):
		pass

	timeOffset = getset_descriptor
	def update(*argv):
		"""update()
Make sure that the armature will be updated on next graphic frame.
This is automatically done if a KX_ArmatureActuator with mode run is active
or if an action is playing. This function is useful in other cases."""

	visible = getset_descriptor
	worldAngularVelocity = getset_descriptor
	worldLinearVelocity = getset_descriptor
	worldOrientation = getset_descriptor
	worldPosition = getset_descriptor
	worldScale = getset_descriptor
	worldTransform = getset_descriptor

class BL_Shader:
	bindCallbacks = getset_descriptor
	def delSource(*argv):
		"""delSource( )"""

	enabled = getset_descriptor
	def getFragmentProg(*argv):
		"""getFragmentProg( )"""

	def getVertexProg(*argv):
		"""getVertexProg( )"""

	invalid = getset_descriptor
	def isValid(*argv):
		"""isValid()"""

	objectCallbacks = getset_descriptor
	def setAttrib(*argv):
		"""setAttrib(enum)"""

	def setSampler(*argv):
		"""setSampler(name, index)"""

	def setSource(*argv):
		"""setSource(vertexProgram, fragmentProgram, apply)"""

	def setSourceList(*argv):
		"""setSourceList(sources, apply)"""

	def setUniform1f(*argv):
		"""setUniform1f(name, fx)"""

	def setUniform1i(*argv):
		"""setUniform1i(name, ix)"""

	def setUniform2f(*argv):
		"""setUniform2f(name, fx, fy)"""

	def setUniform2i(*argv):
		"""setUniform2i(name, ix, iy)"""

	def setUniform3f(*argv):
		"""setUniform3f(name, fx,fy,fz) """

	def setUniform3i(*argv):
		"""setUniform3i(name, ix,iy,iz) """

	def setUniform4f(*argv):
		"""setUniform4f(name, fx,fy,fz, fw) """

	def setUniform4i(*argv):
		"""setUniform4i(name, ix,iy,iz, iw) """

	def setUniformDef(*argv):
		"""setUniformDef(name, enum)"""

	def setUniformEyef(*argv):
		"""setUniformEyef(name)"""

	def setUniformMatrix3(*argv):
		"""setUniformMatrix3(uniform_name, list[3x3], transpose(row-major=true, col-major=false)"""

	def setUniformMatrix4(*argv):
		"""setUniformMatrix4(uniform_name, mat-4x4, transpose(row-major=true, col-major=false)"""

	def setUniformfv(*argv):
		"""setUniformfv(float (list2 or list3 or list4))"""

	def setUniformiv(*argv):
		"""setUniformiv(uniform_name, (list2 or list3 or list4))"""

	def validate(*argv):
		"""validate()"""


class BL_Texture:
	alpha = getset_descriptor
	bindCode = getset_descriptor
	cubeMap = getset_descriptor
	diffuseFactor = getset_descriptor
	diffuseIntensity = getset_descriptor
	emit = getset_descriptor
	hardness = getset_descriptor
	invalid = getset_descriptor
	ior = getset_descriptor
	lodBias = getset_descriptor
	mirror = getset_descriptor
	name = getset_descriptor
	normal = getset_descriptor
	parallaxBump = getset_descriptor
	parallaxStep = getset_descriptor
	refractionRatio = getset_descriptor
	specularFactor = getset_descriptor
	specularIntensity = getset_descriptor

class CListValue:
	def append(*argv):
		pass

	def count(*argv):
		pass

	def from_id(*argv):
		pass

	def get(*argv):
		pass

	def index(*argv):
		pass

	invalid = getset_descriptor
	name = getset_descriptor
	def reverse(*argv):
		pass


class CListWrapper:
	def get(*argv):
		pass

	invalid = getset_descriptor
	name = getset_descriptor

class CValue:
	invalid = getset_descriptor
	name = getset_descriptor

class KX_2DFilter:
	bindCallbacks = getset_descriptor
	def delSource(*argv):
		"""delSource( )"""

	enabled = getset_descriptor
	def getFragmentProg(*argv):
		"""getFragmentProg( )"""

	def getVertexProg(*argv):
		"""getVertexProg( )"""

	invalid = getset_descriptor
	def isValid(*argv):
		"""isValid()"""

	objectCallbacks = getset_descriptor
	def setAttrib(*argv):
		"""setAttrib(enum)"""

	def setSampler(*argv):
		"""setSampler(name, index)"""

	def setSource(*argv):
		"""setSource(vertexProgram, fragmentProgram, apply)"""

	def setSourceList(*argv):
		"""setSourceList(sources, apply)"""

	def setTexture(*argv):
		"""setTexture(index, bindCode, samplerName)"""

	def setUniform1f(*argv):
		"""setUniform1f(name, fx)"""

	def setUniform1i(*argv):
		"""setUniform1i(name, ix)"""

	def setUniform2f(*argv):
		"""setUniform2f(name, fx, fy)"""

	def setUniform2i(*argv):
		"""setUniform2i(name, ix, iy)"""

	def setUniform3f(*argv):
		"""setUniform3f(name, fx,fy,fz) """

	def setUniform3i(*argv):
		"""setUniform3i(name, ix,iy,iz) """

	def setUniform4f(*argv):
		"""setUniform4f(name, fx,fy,fz, fw) """

	def setUniform4i(*argv):
		"""setUniform4i(name, ix,iy,iz, iw) """

	def setUniformDef(*argv):
		"""setUniformDef(name, enum)"""

	def setUniformEyef(*argv):
		"""setUniformEyef(name)"""

	def setUniformMatrix3(*argv):
		"""setUniformMatrix3(uniform_name, list[3x3], transpose(row-major=true, col-major=false)"""

	def setUniformMatrix4(*argv):
		"""setUniformMatrix4(uniform_name, mat-4x4, transpose(row-major=true, col-major=false)"""

	def setUniformfv(*argv):
		"""setUniformfv(float (list2 or list3 or list4))"""

	def setUniformiv(*argv):
		"""setUniformiv(uniform_name, (list2 or list3 or list4))"""

	def validate(*argv):
		"""validate()"""


class KX_2DFilterManager:
	def addFilter(*argv):
		"""addFilter(index, type, fragmentProgram)"""

	def getFilter(*argv):
		"""getFilter(index)"""

	invalid = getset_descriptor
	def removeFilter(*argv):
		"""removeFilter(index)"""


class KX_ArmatureSensor:
	constraint = getset_descriptor
	executePriority = getset_descriptor
	frequency = getset_descriptor
	invalid = getset_descriptor
	invert = getset_descriptor
	level = getset_descriptor
	name = getset_descriptor
	neg_ticks = getset_descriptor
	owner = getset_descriptor
	pos_ticks = getset_descriptor
	positive = getset_descriptor
	def reset(*argv):
		"""reset()
Reset sensor internal state, effect depends on the type of sensor and settings.
The sensor is put in its initial state as if it was just activated."""

	skippedTicks = getset_descriptor
	status = getset_descriptor
	tap = getset_descriptor
	triggered = getset_descriptor
	type = getset_descriptor
	useNegPulseMode = getset_descriptor
	usePosPulseMode = getset_descriptor
	value = getset_descriptor

class KX_BlenderMaterial:
	alpha = getset_descriptor
	ambient = getset_descriptor
	blending = getset_descriptor
	diffuseColor = getset_descriptor
	diffuseIntensity = getset_descriptor
	emit = getset_descriptor
	def getShader(*argv):
		"""getShader()"""

	def getTextureBindcode(*argv):
		"""getTextureBindcode(texslot)"""

	hardness = getset_descriptor
	invalid = getset_descriptor
	name = getset_descriptor
	def setBlending(*argv):
		"""setBlending(bge.logic.src, bge.logic.dest)"""

	shader = getset_descriptor
	specularAlpha = getset_descriptor
	specularColor = getset_descriptor
	specularIntensity = getset_descriptor
	textures = getset_descriptor

class KX_BoundingBox:
	autoUpdate = getset_descriptor
	center = getset_descriptor
	invalid = getset_descriptor
	max = getset_descriptor
	min = getset_descriptor
	radius = getset_descriptor

class KX_Camera:
	INSIDE = getset_descriptor
	INTERSECT = getset_descriptor
	OUTSIDE = getset_descriptor
	actuators = getset_descriptor
	def addDebugProperty(*argv):
		"""addDebugProperty(name, visible=1)
Added or remove a debug property to the debug list."""

	def alignAxisToVect(*argv):
		pass

	angularDamping = getset_descriptor
	angularVelocity = getset_descriptor
	angularVelocityMax = getset_descriptor
	angularVelocityMin = getset_descriptor
	def applyForce(*argv):
		pass

	def applyImpulse(*argv):
		pass

	def applyMovement(*argv):
		pass

	def applyRotation(*argv):
		pass

	def applyTorque(*argv):
		pass

	attrDict = getset_descriptor
	def boxInsideFrustum(*argv):
		"""boxInsideFrustum(box) -> Integer
returns INSIDE, OUTSIDE or INTERSECT if the given box is
inside/outside/intersects this camera's viewing frustum.

box = a list of the eight (8) corners of the box (in world coordinates.)

Example:
import bge.logic

co = bge.logic.getCurrentController()
cam = co.GetOwner()

box = []
box.append([-1.0, -1.0, -1.0])
box.append([-1.0, -1.0,  1.0])
box.append([-1.0,  1.0, -1.0])
box.append([-1.0,  1.0,  1.0])
box.append([ 1.0, -1.0, -1.0])
box.append([ 1.0, -1.0,  1.0])
box.append([ 1.0,  1.0, -1.0])
box.append([ 1.0,  1.0,  1.0])

if (cam.boxInsideFrustum(box) != cam.OUTSIDE):
        # Box is inside/intersects frustum !
        # Do something useful !
else:
        # Box is outside the frustum !"""

	camera_to_world = getset_descriptor
	children = getset_descriptor
	childrenRecursive = getset_descriptor
	collisionCallbacks = getset_descriptor
	collisionGroup = getset_descriptor
	collisionMask = getset_descriptor
	color = getset_descriptor
	components = getset_descriptor
	controllers = getset_descriptor
	culled = getset_descriptor
	cullingBox = getset_descriptor
	currentLodLevel = getset_descriptor
	debug = getset_descriptor
	debugRecursive = getset_descriptor
	def disableRigidBody(*argv):
		pass

	def enableRigidBody(*argv):
		pass

	def endObject(*argv):
		pass

	far = getset_descriptor
	fov = getset_descriptor
	frustum_culling = getset_descriptor
	def get(*argv):
		pass

	def getActionFrame(*argv):
		"""getActionFrame(layer=0)
Gets the current frame of the action playing in the supplied layer"""

	def getActionName(*argv):
		"""getActionName(layer=0)
Gets the name of the current action playing in the supplied layer"""

	def getAngularVelocity(*argv):
		pass

	def getAxisVect(*argv):
		pass

	def getCameraToWorld(*argv):
		"""getCameraToWorld() -> Matrix4x4
returns the camera to world transformation matrix, as a list of four lists of four values.

ie: [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]])"""

	def getDistanceTo(*argv):
		"""getDistanceTo(other): get distance to another point/KX_GameObject"""

	def getLinearVelocity(*argv):
		pass

	def getPhysicsId(*argv):
		pass

	def getPropertyNames(*argv):
		pass

	def getReactionForce(*argv):
		pass

	def getScreenPosition(*argv):
		"""getScreenPosition()"""

	def getScreenRay(*argv):
		"""getScreenRay()"""

	def getScreenVect(*argv):
		"""getScreenVect()"""

	def getVectTo(*argv):
		"""getVectTo(other): get vector and the distance to another point/KX_GameObject
Returns a 3-tuple with (distance,worldVector,localVector)"""

	def getVelocity(*argv):
		pass

	def getWorldToCamera(*argv):
		"""getWorldToCamera() -> Matrix4x4
returns the world to camera transformation matrix, as a list of four lists of four values.

ie: [[1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]])"""

	groupMembers = getset_descriptor
	groupObject = getset_descriptor
	invalid = getset_descriptor
	def isPlayingAction(*argv):
		"""isPlayingAction(layer=0)
Checks to see if there is an action playing in the given layer"""

	isSuspendDynamics = getset_descriptor
	lens = getset_descriptor
	life = getset_descriptor
	linVelocityMax = getset_descriptor
	linVelocityMin = getset_descriptor
	linearDamping = getset_descriptor
	linearVelocity = getset_descriptor
	localAngularVelocity = getset_descriptor
	localInertia = getset_descriptor
	localLinearVelocity = getset_descriptor
	localOrientation = getset_descriptor
	localPosition = getset_descriptor
	localScale = getset_descriptor
	localTransform = getset_descriptor
	lodDistanceFactor = getset_descriptor
	lodManager = getset_descriptor
	mass = getset_descriptor
	meshes = getset_descriptor
	modelview_matrix = getset_descriptor
	name = getset_descriptor
	near = getset_descriptor
	occlusion = getset_descriptor
	orientation = getset_descriptor
	ortho_scale = getset_descriptor
	parent = getset_descriptor
	perspective = getset_descriptor
	def playAction(*argv):
		"""playAction(name, start_frame, end_frame, layer=0, priority=0 blendin=0, play_mode=ACT_MODE_PLAY, layer_weight=0.0, ipo_flags=0, speed=1.0)
Plays an action"""

	def pointInsideFrustum(*argv):
		"""pointInsideFrustum(point) -> Bool
returns 1 if the given point is inside this camera's viewing frustum.

point = The point to test (in world coordinates.)

Example:
import bge.logic

co = bge.logic.getCurrentController()
cam = co.GetOwner()

# Test point [0.0, 0.0, 0.0]    if (cam.pointInsideFrustum([0.0, 0.0, 0.0])):
        # Point is inside frustum !
        # Do something useful !
else:
        # Box is outside the frustum !"""

	position = getset_descriptor
	projection_matrix = getset_descriptor
	def rayCast(*argv):
		"""rayCast(to,from,dist,prop,face,xray,poly,mask): cast a ray and return 3-tuple (object,hit,normal) or 4-tuple (object,hit,normal,polygon) or 4-tuple (object,hit,normal,polygon,hituv) of contact point with object within dist that matches prop.
 If no hit, return (None,None,None) or (None,None,None,None) or (None,None,None,None,None).
 to   = 3-tuple or object reference for destination of ray (if object, use center of object)
 from = 3-tuple or object reference for origin of ray (if object, use center of object)
        Can be None or omitted => start from self object center
 dist = max distance to look (can be negative => look behind); 0 or omitted => detect up to to
 prop = property name that object must have; can be omitted => detect any object
 face = normal option: 1=>return face normal; 0 or omitted => normal is oriented towards origin
 xray = X-ray option: 1=>skip objects that don't match prop; 0 or omitted => stop on first object
 poly = polygon option: 1=>return value is a 4-tuple and the 4th element is a KX_PolyProxy object
                           which can be None if hit object has no mesh or if there is no hit
                        2=>return value is a 5-tuple, the 4th element is the KX_PolyProxy object
                           and the 5th element is the vector of UV coordinates at the hit point of the None if there is no UV mapping
        If 0 or omitted, return value is a 3-tuple
 mask = collision mask: the collision mask that ray can hit, 0 < mask < 65536
Note: The object on which you call this method matters: the ray will ignore it.
      prop and xray option interact as follow:
        prop off, xray off: return closest hit or no hit if there is no object on the full extend of the ray
        prop off, xray on : idem
        prop on,  xray off: return closest hit if it matches prop, no hit otherwise
        prop on,  xray on : return closest hit matching prop or no hit if there is no object matching prop on the full extend of the ray"""

	def rayCastTo(*argv):
		"""rayCastTo(other,dist,prop): look towards another point/KX_GameObject and return first object hit within dist that matches prop
prop = property name that object must have; can be omitted => detect any object
dist = max distance to look (can be negative => look behind); 0 or omitted => detect up to other
other = 3-tuple or object reference"""

	def reinstancePhysicsMesh(*argv):
		pass

	def removeParent(*argv):
		pass

	def replaceMesh(*argv):
		pass

	def replacePhysicsShape(*argv):
		pass

	def restoreDynamics(*argv):
		pass

	def restorePhysics(*argv):
		pass

	scaling = getset_descriptor
	scene = getset_descriptor
	def sendMessage(*argv):
		"""sendMessage(subject, [body, to])
sends a message in same manner as a message actuatorsubject = Subject of the message (string)body = Message body (string)to = Name of object to send the message to"""

	sensors = getset_descriptor
	def setActionFrame(*argv):
		"""setActionFrame(frame, layer=0)
Set the current frame of the action playing in the supplied layer"""

	def setAngularVelocity(*argv):
		pass

	def setCollisionMargin(*argv):
		pass

	def setDamping(*argv):
		pass

	def setLinearVelocity(*argv):
		pass

	def setOcclusion(*argv):
		pass

	def setOnTop(*argv):
		"""setOnTop()
Sets this camera's viewport on top"""

	def setParent(*argv):
		pass

	def setViewport(*argv):
		"""setViewport(left, bottom, right, top)
Sets this camera's viewport"""

	def setVisible(*argv):
		pass

	shift_x = getset_descriptor
	shift_y = getset_descriptor
	def sphereInsideFrustum(*argv):
		"""sphereInsideFrustum(center, radius) -> Integer
returns INSIDE, OUTSIDE or INTERSECT if the given sphere is
inside/outside/intersects this camera's viewing frustum.

center = the center of the sphere (in world coordinates.)
radius = the radius of the sphere

Example:
import bge.logic

co = bge.logic.getCurrentController()
cam = co.GetOwner()

# A sphere of radius 4.0 located at [x, y, z] = [1.0, 1.0, 1.0]
if (cam.sphereInsideFrustum([1.0, 1.0, 1.0], 4) != cam.OUTSIDE):
        # Sphere is inside frustum !
        # Do something useful !
else:
        # Sphere is outside frustum"""

	state = getset_descriptor
	def stopAction(*argv):
		"""stopAction(layer=0)
Stop playing the action on the given layer"""

	def suspendDynamics(*argv):
		pass

	def suspendPhysics(*argv):
		pass

	timeOffset = getset_descriptor
	useViewport = getset_descriptor
	visible = getset_descriptor
	worldAngularVelocity = getset_descriptor
	worldLinearVelocity = getset_descriptor
	worldOrientation = getset_descriptor
	worldPosition = getset_descriptor
	worldScale = getset_descriptor
	worldTransform = getset_descriptor
	world_to_camera = getset_descriptor

class KX_CameraActuator:
	axis = getset_descriptor
	damping = getset_descriptor
	executePriority = getset_descriptor
	height = getset_descriptor
	invalid = getset_descriptor
	max = getset_descriptor
	min = getset_descriptor
	name = getset_descriptor
	object = getset_descriptor
	owner = getset_descriptor

class KX_CharacterWrapper:
	gravity = getset_descriptor
	invalid = getset_descriptor
	def jump(*argv):
		"""jump()
makes the character jump."""

	jumpCount = getset_descriptor
	maxJumps = getset_descriptor
	onGround = getset_descriptor
	walkDirection = getset_descriptor

class KX_CollisionContactPoint:
	appliedImpulse = getset_descriptor
	combinedFriction = getset_descriptor
	combinedRestitution = getset_descriptor
	invalid = getset_descriptor
	localPointA = getset_descriptor
	localPointB = getset_descriptor
	name = getset_descriptor
	normal = getset_descriptor
	worldPoint = getset_descriptor

class KX_CollisionSensor:
	executePriority = getset_descriptor
	frequency = getset_descriptor
	hitMaterial = getset_descriptor
	hitObject = getset_descriptor
	hitObjectList = getset_descriptor
	invalid = getset_descriptor
	invert = getset_descriptor
	level = getset_descriptor
	name = getset_descriptor
	neg_ticks = getset_descriptor
	owner = getset_descriptor
	pos_ticks = getset_descriptor
	positive = getset_descriptor
	propName = getset_descriptor
	def reset(*argv):
		"""reset()
Reset sensor internal state, effect depends on the type of sensor and settings.
The sensor is put in its initial state as if it was just activated."""

	skippedTicks = getset_descriptor
	status = getset_descriptor
	tap = getset_descriptor
	triggered = getset_descriptor
	useMaterial = getset_descriptor
	useNegPulseMode = getset_descriptor
	usePosPulseMode = getset_descriptor
	usePulseCollision = getset_descriptor

class KX_ConstraintActuator:
	damp = getset_descriptor
	direction = getset_descriptor
	distance = getset_descriptor
	executePriority = getset_descriptor
	invalid = getset_descriptor
	limit = getset_descriptor
	max = getset_descriptor
	min = getset_descriptor
	name = getset_descriptor
	option = getset_descriptor
	owner = getset_descriptor
	propName = getset_descriptor
	rayLength = getset_descriptor
	rotDamp = getset_descriptor
	time = getset_descriptor

class KX_ConstraintWrapper:
	constraint_id = getset_descriptor
	constraint_type = getset_descriptor
	def getConstraintId(*argv):
		pass

	def getParam(*argv):
		pass

	invalid = getset_descriptor
	def setParam(*argv):
		pass


class KX_CubeMap:
	autoUpdate = getset_descriptor
	clipEnd = getset_descriptor
	clipStart = getset_descriptor
	enabled = getset_descriptor
	ignoreLayers = getset_descriptor
	invalid = getset_descriptor
	name = getset_descriptor
	def update(*argv):
		"""update(): Set the cube map to be updated next frame."""

	viewpointObject = getset_descriptor

class KX_FontObject:
	actuators = getset_descriptor
	def addDebugProperty(*argv):
		"""addDebugProperty(name, visible=1)
Added or remove a debug property to the debug list."""

	def alignAxisToVect(*argv):
		pass

	angularDamping = getset_descriptor
	angularVelocity = getset_descriptor
	angularVelocityMax = getset_descriptor
	angularVelocityMin = getset_descriptor
	def applyForce(*argv):
		pass

	def applyImpulse(*argv):
		pass

	def applyMovement(*argv):
		pass

	def applyRotation(*argv):
		pass

	def applyTorque(*argv):
		pass

	attrDict = getset_descriptor
	children = getset_descriptor
	childrenRecursive = getset_descriptor
	collisionCallbacks = getset_descriptor
	collisionGroup = getset_descriptor
	collisionMask = getset_descriptor
	color = getset_descriptor
	components = getset_descriptor
	controllers = getset_descriptor
	culled = getset_descriptor
	cullingBox = getset_descriptor
	currentLodLevel = getset_descriptor
	debug = getset_descriptor
	debugRecursive = getset_descriptor
	dimensions = getset_descriptor
	def disableRigidBody(*argv):
		pass

	def enableRigidBody(*argv):
		pass

	def endObject(*argv):
		pass

	def get(*argv):
		pass

	def getActionFrame(*argv):
		"""getActionFrame(layer=0)
Gets the current frame of the action playing in the supplied layer"""

	def getActionName(*argv):
		"""getActionName(layer=0)
Gets the name of the current action playing in the supplied layer"""

	def getAngularVelocity(*argv):
		pass

	def getAxisVect(*argv):
		pass

	def getDistanceTo(*argv):
		"""getDistanceTo(other): get distance to another point/KX_GameObject"""

	def getLinearVelocity(*argv):
		pass

	def getPhysicsId(*argv):
		pass

	def getPropertyNames(*argv):
		pass

	def getReactionForce(*argv):
		pass

	def getVectTo(*argv):
		"""getVectTo(other): get vector and the distance to another point/KX_GameObject
Returns a 3-tuple with (distance,worldVector,localVector)"""

	def getVelocity(*argv):
		pass

	groupMembers = getset_descriptor
	groupObject = getset_descriptor
	invalid = getset_descriptor
	def isPlayingAction(*argv):
		"""isPlayingAction(layer=0)
Checks to see if there is an action playing in the given layer"""

	isSuspendDynamics = getset_descriptor
	life = getset_descriptor
	linVelocityMax = getset_descriptor
	linVelocityMin = getset_descriptor
	linearDamping = getset_descriptor
	linearVelocity = getset_descriptor
	localAngularVelocity = getset_descriptor
	localInertia = getset_descriptor
	localLinearVelocity = getset_descriptor
	localOrientation = getset_descriptor
	localPosition = getset_descriptor
	localScale = getset_descriptor
	localTransform = getset_descriptor
	lodManager = getset_descriptor
	mass = getset_descriptor
	meshes = getset_descriptor
	name = getset_descriptor
	occlusion = getset_descriptor
	orientation = getset_descriptor
	parent = getset_descriptor
	def playAction(*argv):
		"""playAction(name, start_frame, end_frame, layer=0, priority=0 blendin=0, play_mode=ACT_MODE_PLAY, layer_weight=0.0, ipo_flags=0, speed=1.0)
Plays an action"""

	position = getset_descriptor
	def rayCast(*argv):
		"""rayCast(to,from,dist,prop,face,xray,poly,mask): cast a ray and return 3-tuple (object,hit,normal) or 4-tuple (object,hit,normal,polygon) or 4-tuple (object,hit,normal,polygon,hituv) of contact point with object within dist that matches prop.
 If no hit, return (None,None,None) or (None,None,None,None) or (None,None,None,None,None).
 to   = 3-tuple or object reference for destination of ray (if object, use center of object)
 from = 3-tuple or object reference for origin of ray (if object, use center of object)
        Can be None or omitted => start from self object center
 dist = max distance to look (can be negative => look behind); 0 or omitted => detect up to to
 prop = property name that object must have; can be omitted => detect any object
 face = normal option: 1=>return face normal; 0 or omitted => normal is oriented towards origin
 xray = X-ray option: 1=>skip objects that don't match prop; 0 or omitted => stop on first object
 poly = polygon option: 1=>return value is a 4-tuple and the 4th element is a KX_PolyProxy object
                           which can be None if hit object has no mesh or if there is no hit
                        2=>return value is a 5-tuple, the 4th element is the KX_PolyProxy object
                           and the 5th element is the vector of UV coordinates at the hit point of the None if there is no UV mapping
        If 0 or omitted, return value is a 3-tuple
 mask = collision mask: the collision mask that ray can hit, 0 < mask < 65536
Note: The object on which you call this method matters: the ray will ignore it.
      prop and xray option interact as follow:
        prop off, xray off: return closest hit or no hit if there is no object on the full extend of the ray
        prop off, xray on : idem
        prop on,  xray off: return closest hit if it matches prop, no hit otherwise
        prop on,  xray on : return closest hit matching prop or no hit if there is no object matching prop on the full extend of the ray"""

	def rayCastTo(*argv):
		"""rayCastTo(other,dist,prop): look towards another point/KX_GameObject and return first object hit within dist that matches prop
prop = property name that object must have; can be omitted => detect any object
dist = max distance to look (can be negative => look behind); 0 or omitted => detect up to other
other = 3-tuple or object reference"""

	def reinstancePhysicsMesh(*argv):
		pass

	def removeParent(*argv):
		pass

	def replaceMesh(*argv):
		pass

	def replacePhysicsShape(*argv):
		pass

	resolution = getset_descriptor
	def restoreDynamics(*argv):
		pass

	def restorePhysics(*argv):
		pass

	scaling = getset_descriptor
	scene = getset_descriptor
	def sendMessage(*argv):
		"""sendMessage(subject, [body, to])
sends a message in same manner as a message actuatorsubject = Subject of the message (string)body = Message body (string)to = Name of object to send the message to"""

	sensors = getset_descriptor
	def setActionFrame(*argv):
		"""setActionFrame(frame, layer=0)
Set the current frame of the action playing in the supplied layer"""

	def setAngularVelocity(*argv):
		pass

	def setCollisionMargin(*argv):
		pass

	def setDamping(*argv):
		pass

	def setLinearVelocity(*argv):
		pass

	def setOcclusion(*argv):
		pass

	def setParent(*argv):
		pass

	def setVisible(*argv):
		pass

	size = getset_descriptor
	state = getset_descriptor
	def stopAction(*argv):
		"""stopAction(layer=0)
Stop playing the action on the given layer"""

	def suspendDynamics(*argv):
		pass

	def suspendPhysics(*argv):
		pass

	text = getset_descriptor
	timeOffset = getset_descriptor
	visible = getset_descriptor
	worldAngularVelocity = getset_descriptor
	worldLinearVelocity = getset_descriptor
	worldOrientation = getset_descriptor
	worldPosition = getset_descriptor
	worldScale = getset_descriptor
	worldTransform = getset_descriptor

class KX_GameActuator:
	executePriority = getset_descriptor
	fileName = getset_descriptor
	invalid = getset_descriptor
	mode = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor

class KX_GameObject:
	actuators = getset_descriptor
	def addDebugProperty(*argv):
		"""addDebugProperty(name, visible=1)
Added or remove a debug property to the debug list."""

	def alignAxisToVect(*argv):
		pass

	angularDamping = getset_descriptor
	angularVelocity = getset_descriptor
	angularVelocityMax = getset_descriptor
	angularVelocityMin = getset_descriptor
	def applyForce(*argv):
		pass

	def applyImpulse(*argv):
		pass

	def applyMovement(*argv):
		pass

	def applyRotation(*argv):
		pass

	def applyTorque(*argv):
		pass

	attrDict = getset_descriptor
	children = getset_descriptor
	childrenRecursive = getset_descriptor
	collisionCallbacks = getset_descriptor
	collisionGroup = getset_descriptor
	collisionMask = getset_descriptor
	color = getset_descriptor
	components = getset_descriptor
	controllers = getset_descriptor
	culled = getset_descriptor
	cullingBox = getset_descriptor
	currentLodLevel = getset_descriptor
	debug = getset_descriptor
	debugRecursive = getset_descriptor
	def disableRigidBody(*argv):
		pass

	def enableRigidBody(*argv):
		pass

	def endObject(*argv):
		pass

	def get(*argv):
		pass

	def getActionFrame(*argv):
		"""getActionFrame(layer=0)
Gets the current frame of the action playing in the supplied layer"""

	def getActionName(*argv):
		"""getActionName(layer=0)
Gets the name of the current action playing in the supplied layer"""

	def getAngularVelocity(*argv):
		pass

	def getAxisVect(*argv):
		pass

	def getDistanceTo(*argv):
		"""getDistanceTo(other): get distance to another point/KX_GameObject"""

	def getLinearVelocity(*argv):
		pass

	def getPhysicsId(*argv):
		pass

	def getPropertyNames(*argv):
		pass

	def getReactionForce(*argv):
		pass

	def getVectTo(*argv):
		"""getVectTo(other): get vector and the distance to another point/KX_GameObject
Returns a 3-tuple with (distance,worldVector,localVector)"""

	def getVelocity(*argv):
		pass

	groupMembers = getset_descriptor
	groupObject = getset_descriptor
	invalid = getset_descriptor
	def isPlayingAction(*argv):
		"""isPlayingAction(layer=0)
Checks to see if there is an action playing in the given layer"""

	isSuspendDynamics = getset_descriptor
	life = getset_descriptor
	linVelocityMax = getset_descriptor
	linVelocityMin = getset_descriptor
	linearDamping = getset_descriptor
	linearVelocity = getset_descriptor
	localAngularVelocity = getset_descriptor
	localInertia = getset_descriptor
	localLinearVelocity = getset_descriptor
	localOrientation = getset_descriptor
	localPosition = getset_descriptor
	localScale = getset_descriptor
	localTransform = getset_descriptor
	lodManager = getset_descriptor
	mass = getset_descriptor
	meshes = getset_descriptor
	name = getset_descriptor
	occlusion = getset_descriptor
	orientation = getset_descriptor
	parent = getset_descriptor
	def playAction(*argv):
		"""playAction(name, start_frame, end_frame, layer=0, priority=0 blendin=0, play_mode=ACT_MODE_PLAY, layer_weight=0.0, ipo_flags=0, speed=1.0)
Plays an action"""

	position = getset_descriptor
	def rayCast(*argv):
		"""rayCast(to,from,dist,prop,face,xray,poly,mask): cast a ray and return 3-tuple (object,hit,normal) or 4-tuple (object,hit,normal,polygon) or 4-tuple (object,hit,normal,polygon,hituv) of contact point with object within dist that matches prop.
 If no hit, return (None,None,None) or (None,None,None,None) or (None,None,None,None,None).
 to   = 3-tuple or object reference for destination of ray (if object, use center of object)
 from = 3-tuple or object reference for origin of ray (if object, use center of object)
        Can be None or omitted => start from self object center
 dist = max distance to look (can be negative => look behind); 0 or omitted => detect up to to
 prop = property name that object must have; can be omitted => detect any object
 face = normal option: 1=>return face normal; 0 or omitted => normal is oriented towards origin
 xray = X-ray option: 1=>skip objects that don't match prop; 0 or omitted => stop on first object
 poly = polygon option: 1=>return value is a 4-tuple and the 4th element is a KX_PolyProxy object
                           which can be None if hit object has no mesh or if there is no hit
                        2=>return value is a 5-tuple, the 4th element is the KX_PolyProxy object
                           and the 5th element is the vector of UV coordinates at the hit point of the None if there is no UV mapping
        If 0 or omitted, return value is a 3-tuple
 mask = collision mask: the collision mask that ray can hit, 0 < mask < 65536
Note: The object on which you call this method matters: the ray will ignore it.
      prop and xray option interact as follow:
        prop off, xray off: return closest hit or no hit if there is no object on the full extend of the ray
        prop off, xray on : idem
        prop on,  xray off: return closest hit if it matches prop, no hit otherwise
        prop on,  xray on : return closest hit matching prop or no hit if there is no object matching prop on the full extend of the ray"""

	def rayCastTo(*argv):
		"""rayCastTo(other,dist,prop): look towards another point/KX_GameObject and return first object hit within dist that matches prop
prop = property name that object must have; can be omitted => detect any object
dist = max distance to look (can be negative => look behind); 0 or omitted => detect up to other
other = 3-tuple or object reference"""

	def reinstancePhysicsMesh(*argv):
		pass

	def removeParent(*argv):
		pass

	def replaceMesh(*argv):
		pass

	def replacePhysicsShape(*argv):
		pass

	def restoreDynamics(*argv):
		pass

	def restorePhysics(*argv):
		pass

	scaling = getset_descriptor
	scene = getset_descriptor
	def sendMessage(*argv):
		"""sendMessage(subject, [body, to])
sends a message in same manner as a message actuatorsubject = Subject of the message (string)body = Message body (string)to = Name of object to send the message to"""

	sensors = getset_descriptor
	def setActionFrame(*argv):
		"""setActionFrame(frame, layer=0)
Set the current frame of the action playing in the supplied layer"""

	def setAngularVelocity(*argv):
		pass

	def setCollisionMargin(*argv):
		pass

	def setDamping(*argv):
		pass

	def setLinearVelocity(*argv):
		pass

	def setOcclusion(*argv):
		pass

	def setParent(*argv):
		pass

	def setVisible(*argv):
		pass

	state = getset_descriptor
	def stopAction(*argv):
		"""stopAction(layer=0)
Stop playing the action on the given layer"""

	def suspendDynamics(*argv):
		pass

	def suspendPhysics(*argv):
		pass

	timeOffset = getset_descriptor
	visible = getset_descriptor
	worldAngularVelocity = getset_descriptor
	worldLinearVelocity = getset_descriptor
	worldOrientation = getset_descriptor
	worldPosition = getset_descriptor
	worldScale = getset_descriptor
	worldTransform = getset_descriptor

class KX_LibLoadStatus:
	finished = getset_descriptor
	invalid = getset_descriptor
	libraryName = getset_descriptor
	onFinish = getset_descriptor
	progress = getset_descriptor
	timeTaken = getset_descriptor

class KX_LightObject:
	HEMI = getset_descriptor
	NORMAL = getset_descriptor
	SPOT = getset_descriptor
	SUN = getset_descriptor
	actuators = getset_descriptor
	def addDebugProperty(*argv):
		"""addDebugProperty(name, visible=1)
Added or remove a debug property to the debug list."""

	def alignAxisToVect(*argv):
		pass

	angularDamping = getset_descriptor
	angularVelocity = getset_descriptor
	angularVelocityMax = getset_descriptor
	angularVelocityMin = getset_descriptor
	def applyForce(*argv):
		pass

	def applyImpulse(*argv):
		pass

	def applyMovement(*argv):
		pass

	def applyRotation(*argv):
		pass

	def applyTorque(*argv):
		pass

	attrDict = getset_descriptor
	children = getset_descriptor
	childrenRecursive = getset_descriptor
	collisionCallbacks = getset_descriptor
	collisionGroup = getset_descriptor
	collisionMask = getset_descriptor
	color = getset_descriptor
	components = getset_descriptor
	controllers = getset_descriptor
	culled = getset_descriptor
	cullingBox = getset_descriptor
	currentLodLevel = getset_descriptor
	debug = getset_descriptor
	debugRecursive = getset_descriptor
	def disableRigidBody(*argv):
		pass

	distance = getset_descriptor
	def enableRigidBody(*argv):
		pass

	def endObject(*argv):
		pass

	energy = getset_descriptor
	def get(*argv):
		pass

	def getActionFrame(*argv):
		"""getActionFrame(layer=0)
Gets the current frame of the action playing in the supplied layer"""

	def getActionName(*argv):
		"""getActionName(layer=0)
Gets the name of the current action playing in the supplied layer"""

	def getAngularVelocity(*argv):
		pass

	def getAxisVect(*argv):
		pass

	def getDistanceTo(*argv):
		"""getDistanceTo(other): get distance to another point/KX_GameObject"""

	def getLinearVelocity(*argv):
		pass

	def getPhysicsId(*argv):
		pass

	def getPropertyNames(*argv):
		pass

	def getReactionForce(*argv):
		pass

	def getVectTo(*argv):
		"""getVectTo(other): get vector and the distance to another point/KX_GameObject
Returns a 3-tuple with (distance,worldVector,localVector)"""

	def getVelocity(*argv):
		pass

	groupMembers = getset_descriptor
	groupObject = getset_descriptor
	invalid = getset_descriptor
	def isPlayingAction(*argv):
		"""isPlayingAction(layer=0)
Checks to see if there is an action playing in the given layer"""

	isSuspendDynamics = getset_descriptor
	layer = getset_descriptor
	life = getset_descriptor
	linVelocityMax = getset_descriptor
	linVelocityMin = getset_descriptor
	lin_attenuation = getset_descriptor
	linearDamping = getset_descriptor
	linearVelocity = getset_descriptor
	localAngularVelocity = getset_descriptor
	localInertia = getset_descriptor
	localLinearVelocity = getset_descriptor
	localOrientation = getset_descriptor
	localPosition = getset_descriptor
	localScale = getset_descriptor
	localTransform = getset_descriptor
	lodManager = getset_descriptor
	mass = getset_descriptor
	meshes = getset_descriptor
	name = getset_descriptor
	occlusion = getset_descriptor
	orientation = getset_descriptor
	parent = getset_descriptor
	def playAction(*argv):
		"""playAction(name, start_frame, end_frame, layer=0, priority=0 blendin=0, play_mode=ACT_MODE_PLAY, layer_weight=0.0, ipo_flags=0, speed=1.0)
Plays an action"""

	position = getset_descriptor
	quad_attenuation = getset_descriptor
	def rayCast(*argv):
		"""rayCast(to,from,dist,prop,face,xray,poly,mask): cast a ray and return 3-tuple (object,hit,normal) or 4-tuple (object,hit,normal,polygon) or 4-tuple (object,hit,normal,polygon,hituv) of contact point with object within dist that matches prop.
 If no hit, return (None,None,None) or (None,None,None,None) or (None,None,None,None,None).
 to   = 3-tuple or object reference for destination of ray (if object, use center of object)
 from = 3-tuple or object reference for origin of ray (if object, use center of object)
        Can be None or omitted => start from self object center
 dist = max distance to look (can be negative => look behind); 0 or omitted => detect up to to
 prop = property name that object must have; can be omitted => detect any object
 face = normal option: 1=>return face normal; 0 or omitted => normal is oriented towards origin
 xray = X-ray option: 1=>skip objects that don't match prop; 0 or omitted => stop on first object
 poly = polygon option: 1=>return value is a 4-tuple and the 4th element is a KX_PolyProxy object
                           which can be None if hit object has no mesh or if there is no hit
                        2=>return value is a 5-tuple, the 4th element is the KX_PolyProxy object
                           and the 5th element is the vector of UV coordinates at the hit point of the None if there is no UV mapping
        If 0 or omitted, return value is a 3-tuple
 mask = collision mask: the collision mask that ray can hit, 0 < mask < 65536
Note: The object on which you call this method matters: the ray will ignore it.
      prop and xray option interact as follow:
        prop off, xray off: return closest hit or no hit if there is no object on the full extend of the ray
        prop off, xray on : idem
        prop on,  xray off: return closest hit if it matches prop, no hit otherwise
        prop on,  xray on : return closest hit matching prop or no hit if there is no object matching prop on the full extend of the ray"""

	def rayCastTo(*argv):
		"""rayCastTo(other,dist,prop): look towards another point/KX_GameObject and return first object hit within dist that matches prop
prop = property name that object must have; can be omitted => detect any object
dist = max distance to look (can be negative => look behind); 0 or omitted => detect up to other
other = 3-tuple or object reference"""

	def reinstancePhysicsMesh(*argv):
		pass

	def removeParent(*argv):
		pass

	def replaceMesh(*argv):
		pass

	def replacePhysicsShape(*argv):
		pass

	def restoreDynamics(*argv):
		pass

	def restorePhysics(*argv):
		pass

	scaling = getset_descriptor
	scene = getset_descriptor
	def sendMessage(*argv):
		"""sendMessage(subject, [body, to])
sends a message in same manner as a message actuatorsubject = Subject of the message (string)body = Message body (string)to = Name of object to send the message to"""

	sensors = getset_descriptor
	def setActionFrame(*argv):
		"""setActionFrame(frame, layer=0)
Set the current frame of the action playing in the supplied layer"""

	def setAngularVelocity(*argv):
		pass

	def setCollisionMargin(*argv):
		pass

	def setDamping(*argv):
		pass

	def setLinearVelocity(*argv):
		pass

	def setOcclusion(*argv):
		pass

	def setParent(*argv):
		pass

	def setVisible(*argv):
		pass

	shadowBias = getset_descriptor
	shadowBindId = getset_descriptor
	shadowBleedBias = getset_descriptor
	shadowClipEnd = getset_descriptor
	shadowClipStart = getset_descriptor
	shadowColor = getset_descriptor
	shadowFrustumSize = getset_descriptor
	shadowMapType = getset_descriptor
	shadowMatrix = getset_descriptor
	spotblend = getset_descriptor
	spotsize = getset_descriptor
	state = getset_descriptor
	staticShadow = getset_descriptor
	def stopAction(*argv):
		"""stopAction(layer=0)
Stop playing the action on the given layer"""

	def suspendDynamics(*argv):
		pass

	def suspendPhysics(*argv):
		pass

	timeOffset = getset_descriptor
	type = getset_descriptor
	def updateShadow(*argv):
		"""updateShadow(): Set the shadow to be updated next frame if the lamp uses a static shadow."""

	useShadow = getset_descriptor
	visible = getset_descriptor
	worldAngularVelocity = getset_descriptor
	worldLinearVelocity = getset_descriptor
	worldOrientation = getset_descriptor
	worldPosition = getset_descriptor
	worldScale = getset_descriptor
	worldTransform = getset_descriptor

class KX_LodLevel:
	distance = getset_descriptor
	hysteresis = getset_descriptor
	invalid = getset_descriptor
	level = getset_descriptor
	mesh = getset_descriptor
	name = getset_descriptor
	useHysteresis = getset_descriptor
	useMaterial = getset_descriptor
	useMesh = getset_descriptor

class KX_LodManager:
	distanceFactor = getset_descriptor
	invalid = getset_descriptor
	levels = getset_descriptor
	name = getset_descriptor

class KX_MeshProxy:
	def getMaterialName(*argv):
		pass

	def getPolygon(*argv):
		pass

	def getTextureName(*argv):
		pass

	def getVertex(*argv):
		pass

	def getVertexArrayLength(*argv):
		pass

	invalid = getset_descriptor
	materials = getset_descriptor
	name = getset_descriptor
	numMaterials = getset_descriptor
	numPolygons = getset_descriptor
	polygons = getset_descriptor
	def replaceMaterial(*argv):
		pass

	def transform(*argv):
		pass

	def transformUV(*argv):
		pass


class KX_MouseActuator:
	angle = getset_descriptor
	executePriority = getset_descriptor
	invalid = getset_descriptor
	limit_x = getset_descriptor
	limit_y = getset_descriptor
	local_x = getset_descriptor
	local_y = getset_descriptor
	name = getset_descriptor
	object_axis = getset_descriptor
	owner = getset_descriptor
	def reset(*argv):
		"""reset() : undo rotation caused by actuator"""

	reset_x = getset_descriptor
	reset_y = getset_descriptor
	sensitivity = getset_descriptor
	threshold = getset_descriptor
	use_axis_x = getset_descriptor
	use_axis_y = getset_descriptor
	visible = getset_descriptor

class KX_MouseFocusSensor:
	executePriority = getset_descriptor
	frequency = getset_descriptor
	def getButtonStatus(*argv):
		"""getButtonStatus(button)
Get the given button's status (KX_INPUT_NONE, KX_INPUT_NONE, KX_INPUT_JUST_ACTIVATED, KX_INPUT_ACTIVE, KX_INPUT_JUST_RELEASED)."""

	hitNormal = getset_descriptor
	hitObject = getset_descriptor
	hitPosition = getset_descriptor
	hitUV = getset_descriptor
	invalid = getset_descriptor
	invert = getset_descriptor
	level = getset_descriptor
	mode = getset_descriptor
	name = getset_descriptor
	neg_ticks = getset_descriptor
	owner = getset_descriptor
	pos_ticks = getset_descriptor
	position = getset_descriptor
	positive = getset_descriptor
	propName = getset_descriptor
	rayDirection = getset_descriptor
	raySource = getset_descriptor
	rayTarget = getset_descriptor
	def reset(*argv):
		"""reset()
Reset sensor internal state, effect depends on the type of sensor and settings.
The sensor is put in its initial state as if it was just activated."""

	skippedTicks = getset_descriptor
	status = getset_descriptor
	tap = getset_descriptor
	triggered = getset_descriptor
	useMaterial = getset_descriptor
	useNegPulseMode = getset_descriptor
	usePosPulseMode = getset_descriptor
	usePulseFocus = getset_descriptor
	useXRay = getset_descriptor

class KX_MovementSensor:
	axis = getset_descriptor
	executePriority = getset_descriptor
	frequency = getset_descriptor
	invalid = getset_descriptor
	invert = getset_descriptor
	level = getset_descriptor
	name = getset_descriptor
	neg_ticks = getset_descriptor
	owner = getset_descriptor
	pos_ticks = getset_descriptor
	positive = getset_descriptor
	def reset(*argv):
		"""reset()
Reset sensor internal state, effect depends on the type of sensor and settings.
The sensor is put in its initial state as if it was just activated."""

	skippedTicks = getset_descriptor
	status = getset_descriptor
	tap = getset_descriptor
	threshold = getset_descriptor
	triggered = getset_descriptor
	useNegPulseMode = getset_descriptor
	usePosPulseMode = getset_descriptor

class KX_NavMeshObject:
	actuators = getset_descriptor
	def addDebugProperty(*argv):
		"""addDebugProperty(name, visible=1)
Added or remove a debug property to the debug list."""

	def alignAxisToVect(*argv):
		pass

	angularDamping = getset_descriptor
	angularVelocity = getset_descriptor
	angularVelocityMax = getset_descriptor
	angularVelocityMin = getset_descriptor
	def applyForce(*argv):
		pass

	def applyImpulse(*argv):
		pass

	def applyMovement(*argv):
		pass

	def applyRotation(*argv):
		pass

	def applyTorque(*argv):
		pass

	attrDict = getset_descriptor
	children = getset_descriptor
	childrenRecursive = getset_descriptor
	collisionCallbacks = getset_descriptor
	collisionGroup = getset_descriptor
	collisionMask = getset_descriptor
	color = getset_descriptor
	components = getset_descriptor
	controllers = getset_descriptor
	culled = getset_descriptor
	cullingBox = getset_descriptor
	currentLodLevel = getset_descriptor
	debug = getset_descriptor
	debugRecursive = getset_descriptor
	def disableRigidBody(*argv):
		pass

	def draw(*argv):
		"""draw(mode): navigation mesh debug drawing
mode: WALLS, POLYS, TRIS"""

	def enableRigidBody(*argv):
		pass

	def endObject(*argv):
		pass

	def findPath(*argv):
		"""findPath(start, goal): find path from start to goal points
Returns a path as list of points)"""

	def get(*argv):
		pass

	def getActionFrame(*argv):
		"""getActionFrame(layer=0)
Gets the current frame of the action playing in the supplied layer"""

	def getActionName(*argv):
		"""getActionName(layer=0)
Gets the name of the current action playing in the supplied layer"""

	def getAngularVelocity(*argv):
		pass

	def getAxisVect(*argv):
		pass

	def getDistanceTo(*argv):
		"""getDistanceTo(other): get distance to another point/KX_GameObject"""

	def getLinearVelocity(*argv):
		pass

	def getPhysicsId(*argv):
		pass

	def getPropertyNames(*argv):
		pass

	def getReactionForce(*argv):
		pass

	def getVectTo(*argv):
		"""getVectTo(other): get vector and the distance to another point/KX_GameObject
Returns a 3-tuple with (distance,worldVector,localVector)"""

	def getVelocity(*argv):
		pass

	groupMembers = getset_descriptor
	groupObject = getset_descriptor
	invalid = getset_descriptor
	def isPlayingAction(*argv):
		"""isPlayingAction(layer=0)
Checks to see if there is an action playing in the given layer"""

	isSuspendDynamics = getset_descriptor
	life = getset_descriptor
	linVelocityMax = getset_descriptor
	linVelocityMin = getset_descriptor
	linearDamping = getset_descriptor
	linearVelocity = getset_descriptor
	localAngularVelocity = getset_descriptor
	localInertia = getset_descriptor
	localLinearVelocity = getset_descriptor
	localOrientation = getset_descriptor
	localPosition = getset_descriptor
	localScale = getset_descriptor
	localTransform = getset_descriptor
	lodManager = getset_descriptor
	mass = getset_descriptor
	meshes = getset_descriptor
	name = getset_descriptor
	occlusion = getset_descriptor
	orientation = getset_descriptor
	parent = getset_descriptor
	def playAction(*argv):
		"""playAction(name, start_frame, end_frame, layer=0, priority=0 blendin=0, play_mode=ACT_MODE_PLAY, layer_weight=0.0, ipo_flags=0, speed=1.0)
Plays an action"""

	position = getset_descriptor
	def rayCast(*argv):
		"""rayCast(to,from,dist,prop,face,xray,poly,mask): cast a ray and return 3-tuple (object,hit,normal) or 4-tuple (object,hit,normal,polygon) or 4-tuple (object,hit,normal,polygon,hituv) of contact point with object within dist that matches prop.
 If no hit, return (None,None,None) or (None,None,None,None) or (None,None,None,None,None).
 to   = 3-tuple or object reference for destination of ray (if object, use center of object)
 from = 3-tuple or object reference for origin of ray (if object, use center of object)
        Can be None or omitted => start from self object center
 dist = max distance to look (can be negative => look behind); 0 or omitted => detect up to to
 prop = property name that object must have; can be omitted => detect any object
 face = normal option: 1=>return face normal; 0 or omitted => normal is oriented towards origin
 xray = X-ray option: 1=>skip objects that don't match prop; 0 or omitted => stop on first object
 poly = polygon option: 1=>return value is a 4-tuple and the 4th element is a KX_PolyProxy object
                           which can be None if hit object has no mesh or if there is no hit
                        2=>return value is a 5-tuple, the 4th element is the KX_PolyProxy object
                           and the 5th element is the vector of UV coordinates at the hit point of the None if there is no UV mapping
        If 0 or omitted, return value is a 3-tuple
 mask = collision mask: the collision mask that ray can hit, 0 < mask < 65536
Note: The object on which you call this method matters: the ray will ignore it.
      prop and xray option interact as follow:
        prop off, xray off: return closest hit or no hit if there is no object on the full extend of the ray
        prop off, xray on : idem
        prop on,  xray off: return closest hit if it matches prop, no hit otherwise
        prop on,  xray on : return closest hit matching prop or no hit if there is no object matching prop on the full extend of the ray"""

	def rayCastTo(*argv):
		"""rayCastTo(other,dist,prop): look towards another point/KX_GameObject and return first object hit within dist that matches prop
prop = property name that object must have; can be omitted => detect any object
dist = max distance to look (can be negative => look behind); 0 or omitted => detect up to other
other = 3-tuple or object reference"""

	def raycast(*argv):
		"""raycast(start, goal): raycast from start to goal points
Returns hit factor)"""

	def rebuild(*argv):
		"""rebuild(): rebuild navigation mesh"""

	def reinstancePhysicsMesh(*argv):
		pass

	def removeParent(*argv):
		pass

	def replaceMesh(*argv):
		pass

	def replacePhysicsShape(*argv):
		pass

	def restoreDynamics(*argv):
		pass

	def restorePhysics(*argv):
		pass

	scaling = getset_descriptor
	scene = getset_descriptor
	def sendMessage(*argv):
		"""sendMessage(subject, [body, to])
sends a message in same manner as a message actuatorsubject = Subject of the message (string)body = Message body (string)to = Name of object to send the message to"""

	sensors = getset_descriptor
	def setActionFrame(*argv):
		"""setActionFrame(frame, layer=0)
Set the current frame of the action playing in the supplied layer"""

	def setAngularVelocity(*argv):
		pass

	def setCollisionMargin(*argv):
		pass

	def setDamping(*argv):
		pass

	def setLinearVelocity(*argv):
		pass

	def setOcclusion(*argv):
		pass

	def setParent(*argv):
		pass

	def setVisible(*argv):
		pass

	state = getset_descriptor
	def stopAction(*argv):
		"""stopAction(layer=0)
Stop playing the action on the given layer"""

	def suspendDynamics(*argv):
		pass

	def suspendPhysics(*argv):
		pass

	timeOffset = getset_descriptor
	visible = getset_descriptor
	worldAngularVelocity = getset_descriptor
	worldLinearVelocity = getset_descriptor
	worldOrientation = getset_descriptor
	worldPosition = getset_descriptor
	worldScale = getset_descriptor
	worldTransform = getset_descriptor

class KX_NearSensor:
	distance = getset_descriptor
	executePriority = getset_descriptor
	frequency = getset_descriptor
	hitMaterial = getset_descriptor
	hitObject = getset_descriptor
	hitObjectList = getset_descriptor
	invalid = getset_descriptor
	invert = getset_descriptor
	level = getset_descriptor
	name = getset_descriptor
	neg_ticks = getset_descriptor
	owner = getset_descriptor
	pos_ticks = getset_descriptor
	positive = getset_descriptor
	propName = getset_descriptor
	def reset(*argv):
		"""reset()
Reset sensor internal state, effect depends on the type of sensor and settings.
The sensor is put in its initial state as if it was just activated."""

	resetDistance = getset_descriptor
	skippedTicks = getset_descriptor
	status = getset_descriptor
	tap = getset_descriptor
	triggered = getset_descriptor
	useMaterial = getset_descriptor
	useNegPulseMode = getset_descriptor
	usePosPulseMode = getset_descriptor
	usePulseCollision = getset_descriptor

class KX_NetworkMessageActuator:
	body = getset_descriptor
	executePriority = getset_descriptor
	invalid = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	propName = getset_descriptor
	subject = getset_descriptor
	usePropBody = getset_descriptor

class KX_NetworkMessageSensor:
	bodies = getset_descriptor
	executePriority = getset_descriptor
	frameMessageCount = getset_descriptor
	frequency = getset_descriptor
	invalid = getset_descriptor
	invert = getset_descriptor
	level = getset_descriptor
	name = getset_descriptor
	neg_ticks = getset_descriptor
	owner = getset_descriptor
	pos_ticks = getset_descriptor
	positive = getset_descriptor
	def reset(*argv):
		"""reset()
Reset sensor internal state, effect depends on the type of sensor and settings.
The sensor is put in its initial state as if it was just activated."""

	skippedTicks = getset_descriptor
	status = getset_descriptor
	subject = getset_descriptor
	subjects = getset_descriptor
	tap = getset_descriptor
	triggered = getset_descriptor
	useNegPulseMode = getset_descriptor
	usePosPulseMode = getset_descriptor

class KX_ObjectActuator:
	angV = getset_descriptor
	dLoc = getset_descriptor
	dRot = getset_descriptor
	damping = getset_descriptor
	executePriority = getset_descriptor
	force = getset_descriptor
	forceLimitX = getset_descriptor
	forceLimitY = getset_descriptor
	forceLimitZ = getset_descriptor
	invalid = getset_descriptor
	linV = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	pid = getset_descriptor
	reference = getset_descriptor
	torque = getset_descriptor
	useLocalAngV = getset_descriptor
	useLocalDLoc = getset_descriptor
	useLocalDRot = getset_descriptor
	useLocalForce = getset_descriptor
	useLocalLinV = getset_descriptor
	useLocalTorque = getset_descriptor

class KX_ParentActuator:
	compound = getset_descriptor
	executePriority = getset_descriptor
	ghost = getset_descriptor
	invalid = getset_descriptor
	mode = getset_descriptor
	name = getset_descriptor
	object = getset_descriptor
	owner = getset_descriptor

class KX_PolyProxy:
	collide = getset_descriptor
	def getMaterial(*argv):
		"""getMaterial() : returns a material"""

	def getMaterialIndex(*argv):
		"""getMaterialIndex() : return the material index of the polygon in the mesh"""

	def getMaterialName(*argv):
		"""getMaterialName() : returns the polygon material name, "NoMaterial" if no material"""

	def getMesh(*argv):
		"""getMesh() : returns a mesh proxy"""

	def getNumVertex(*argv):
		"""getNumVertex() : returns the number of vertex of the polygon, 3 or 4"""

	def getTextureName(*argv):
		"""getTexturelName() : returns the polygon texture name, "NULL" if no texture"""

	def getVertexIndex(*argv):
		"""getVertexIndex(vertex) : returns the mesh vertex index of a polygon vertex
vertex: index of the vertex in the polygon: 0->3
return value can be used to retrieve the vertex details through mesh proxy
Note: getVertexIndex(3) on a triangle polygon returns 0"""

	invalid = getset_descriptor
	def isCollider(*argv):
		"""isCollider() : returns whether the polygon is receives collision or not"""

	def isVisible(*argv):
		"""isVisible() : returns whether the polygon is visible or not"""

	material = getset_descriptor
	material_id = getset_descriptor
	material_name = getset_descriptor
	name = getset_descriptor
	texture_name = getset_descriptor
	v1 = getset_descriptor
	v2 = getset_descriptor
	v3 = getset_descriptor
	v4 = getset_descriptor
	vertices = getset_descriptor
	visible = getset_descriptor

class KX_PythonComponent:
	invalid = getset_descriptor
	object = getset_descriptor

class KX_RadarSensor:
	angle = getset_descriptor
	axis = getset_descriptor
	coneOrigin = getset_descriptor
	coneTarget = getset_descriptor
	distance = getset_descriptor
	executePriority = getset_descriptor
	frequency = getset_descriptor
	hitMaterial = getset_descriptor
	hitObject = getset_descriptor
	hitObjectList = getset_descriptor
	invalid = getset_descriptor
	invert = getset_descriptor
	level = getset_descriptor
	name = getset_descriptor
	neg_ticks = getset_descriptor
	owner = getset_descriptor
	pos_ticks = getset_descriptor
	positive = getset_descriptor
	propName = getset_descriptor
	def reset(*argv):
		"""reset()
Reset sensor internal state, effect depends on the type of sensor and settings.
The sensor is put in its initial state as if it was just activated."""

	resetDistance = getset_descriptor
	skippedTicks = getset_descriptor
	status = getset_descriptor
	tap = getset_descriptor
	triggered = getset_descriptor
	useMaterial = getset_descriptor
	useNegPulseMode = getset_descriptor
	usePosPulseMode = getset_descriptor
	usePulseCollision = getset_descriptor

class KX_RaySensor:
	axis = getset_descriptor
	executePriority = getset_descriptor
	frequency = getset_descriptor
	hitMaterial = getset_descriptor
	hitNormal = getset_descriptor
	hitObject = getset_descriptor
	hitPosition = getset_descriptor
	invalid = getset_descriptor
	invert = getset_descriptor
	level = getset_descriptor
	mask = getset_descriptor
	name = getset_descriptor
	neg_ticks = getset_descriptor
	owner = getset_descriptor
	pos_ticks = getset_descriptor
	positive = getset_descriptor
	propName = getset_descriptor
	range = getset_descriptor
	rayDirection = getset_descriptor
	def reset(*argv):
		"""reset()
Reset sensor internal state, effect depends on the type of sensor and settings.
The sensor is put in its initial state as if it was just activated."""

	skippedTicks = getset_descriptor
	status = getset_descriptor
	tap = getset_descriptor
	triggered = getset_descriptor
	useMaterial = getset_descriptor
	useNegPulseMode = getset_descriptor
	usePosPulseMode = getset_descriptor
	useXRay = getset_descriptor

class KX_SCA_AddObjectActuator:
	angularVelocity = getset_descriptor
	executePriority = getset_descriptor
	def instantAddObject(*argv):
		pass

	invalid = getset_descriptor
	linearVelocity = getset_descriptor
	name = getset_descriptor
	object = getset_descriptor
	objectLastCreated = getset_descriptor
	owner = getset_descriptor
	time = getset_descriptor

class KX_SCA_DynamicActuator:
	executePriority = getset_descriptor
	invalid = getset_descriptor
	mass = getset_descriptor
	mode = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor

class KX_SCA_EndObjectActuator:
	executePriority = getset_descriptor
	invalid = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor

class KX_SCA_ReplaceMeshActuator:
	executePriority = getset_descriptor
	def instantReplaceMesh(*argv):
		"""instantReplaceMesh() : immediately replace mesh without delay"""

	invalid = getset_descriptor
	mesh = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	useDisplayMesh = getset_descriptor
	usePhysicsMesh = getset_descriptor

class KX_Scene:
	active_camera = getset_descriptor
	activity_culling = getset_descriptor
	activity_culling_radius = getset_descriptor
	def addObject(*argv):
		"""addObject(object, other, time=0)
Returns the added object."""

	cameras = getset_descriptor
	dbvt_culling = getset_descriptor
	def drawObstacleSimulation(*argv):
		"""drawObstacleSimulation()
Draw debug visualization of obstacle simulation."""

	def end(*argv):
		"""end()
Removes this scene from the game."""

	filterManager = getset_descriptor
	def get(*argv):
		pass

	gravity = getset_descriptor
	invalid = getset_descriptor
	lights = getset_descriptor
	name = getset_descriptor
	objects = getset_descriptor
	objectsInactive = getset_descriptor
	post_draw = getset_descriptor
	pre_draw = getset_descriptor
	pre_draw_setup = getset_descriptor
	def replace(*argv):
		"""replace(newScene)
Replaces this scene with another one.
Return True if the new scene exists and scheduled for replacement, False otherwise."""

	def restart(*argv):
		"""restart()
Restarts this scene."""

	def resume(*argv):
		"""resume()
Resumes this scene."""

	def suspend(*argv):
		"""suspend()
Suspends this scene."""

	suspended = getset_descriptor
	texts = getset_descriptor
	world = getset_descriptor

class KX_SceneActuator:
	camera = getset_descriptor
	executePriority = getset_descriptor
	invalid = getset_descriptor
	mode = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	scene = getset_descriptor
	useRestart = getset_descriptor

class KX_SoundActuator:
	attenuation = getset_descriptor
	cone_angle_inner = getset_descriptor
	cone_angle_outer = getset_descriptor
	cone_volume_outer = getset_descriptor
	distance_maximum = getset_descriptor
	distance_reference = getset_descriptor
	executePriority = getset_descriptor
	invalid = getset_descriptor
	is3D = getset_descriptor
	mode = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	def pauseSound(*argv):
		"""pauseSound()
Pauses the sound."""

	pitch = getset_descriptor
	sound = getset_descriptor
	def startSound(*argv):
		"""startSound()
Starts the sound."""

	def stopSound(*argv):
		"""stopSound()
Stops the sound."""

	time = getset_descriptor
	volume = getset_descriptor
	volume_maximum = getset_descriptor
	volume_minimum = getset_descriptor

class KX_StateActuator:
	executePriority = getset_descriptor
	invalid = getset_descriptor
	mask = getset_descriptor
	name = getset_descriptor
	operation = getset_descriptor
	owner = getset_descriptor

class KX_SteeringActuator:
	acceleration = getset_descriptor
	behavior = getset_descriptor
	distance = getset_descriptor
	enableVisualization = getset_descriptor
	executePriority = getset_descriptor
	facingMode = getset_descriptor
	invalid = getset_descriptor
	lockZVelocity = getset_descriptor
	name = getset_descriptor
	navmesh = getset_descriptor
	owner = getset_descriptor
	path = getset_descriptor
	pathUpdatePeriod = getset_descriptor
	selfterminated = getset_descriptor
	steeringVec = getset_descriptor
	target = getset_descriptor
	turnspeed = getset_descriptor
	velocity = getset_descriptor

class KX_TrackToActuator:
	executePriority = getset_descriptor
	invalid = getset_descriptor
	name = getset_descriptor
	object = getset_descriptor
	owner = getset_descriptor
	time = getset_descriptor
	trackAxis = getset_descriptor
	upAxis = getset_descriptor
	use3D = getset_descriptor

class KX_VehicleWrapper:
	def addWheel(*argv):
		pass

	def applyBraking(*argv):
		pass

	def applyEngineForce(*argv):
		pass

	def getConstraintId(*argv):
		pass

	def getConstraintType(*argv):
		pass

	def getNumWheels(*argv):
		pass

	def getWheelOrientationQuaternion(*argv):
		pass

	def getWheelPosition(*argv):
		pass

	def getWheelRotation(*argv):
		pass

	invalid = getset_descriptor
	rayMask = getset_descriptor
	def setRollInfluence(*argv):
		pass

	def setSteeringValue(*argv):
		pass

	def setSuspensionCompression(*argv):
		pass

	def setSuspensionDamping(*argv):
		pass

	def setSuspensionStiffness(*argv):
		pass

	def setTyreFriction(*argv):
		pass


class KX_VertexProxy:
	UV = getset_descriptor
	XYZ = getset_descriptor
	a = getset_descriptor
	b = getset_descriptor
	color = getset_descriptor
	colors = getset_descriptor
	g = getset_descriptor
	def getNormal(*argv):
		pass

	def getRGBA(*argv):
		pass

	def getUV(*argv):
		pass

	def getUV2(*argv):
		pass

	def getXYZ(*argv):
		pass

	invalid = getset_descriptor
	name = getset_descriptor
	normal = getset_descriptor
	r = getset_descriptor
	def setNormal(*argv):
		pass

	def setRGBA(*argv):
		pass

	def setUV(*argv):
		pass

	def setUV2(*argv):
		pass

	def setXYZ(*argv):
		pass

	u = getset_descriptor
	u2 = getset_descriptor
	uvs = getset_descriptor
	v = getset_descriptor
	v2 = getset_descriptor
	x = getset_descriptor
	y = getset_descriptor
	z = getset_descriptor

class KX_VisibilityActuator:
	executePriority = getset_descriptor
	invalid = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	useOcclusion = getset_descriptor
	useRecursion = getset_descriptor
	visibility = getset_descriptor

class KX_WorldInfo:
	KX_MIST_INV_QUADRATIC = getset_descriptor
	KX_MIST_LINEAR = getset_descriptor
	KX_MIST_QUADRATIC = getset_descriptor
	ambientColor = getset_descriptor
	backgroundColor = getset_descriptor
	exposure = getset_descriptor
	horizonColor = getset_descriptor
	invalid = getset_descriptor
	mistColor = getset_descriptor
	mistDistance = getset_descriptor
	mistEnable = getset_descriptor
	mistIntensity = getset_descriptor
	mistStart = getset_descriptor
	mistType = getset_descriptor
	range = getset_descriptor
	zenithColor = getset_descriptor

class PyObjectPlus:
	invalid = getset_descriptor

class SCA_2DFilterActuator:
	disableMotionBlur = getset_descriptor
	executePriority = getset_descriptor
	invalid = getset_descriptor
	mode = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	passNumber = getset_descriptor
	shaderText = getset_descriptor
	value = getset_descriptor

class SCA_ANDController:
	actuators = getset_descriptor
	executePriority = getset_descriptor
	invalid = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	sensors = getset_descriptor
	state = getset_descriptor
	useHighPriority = getset_descriptor

class SCA_ActuatorSensor:
	actuator = getset_descriptor
	executePriority = getset_descriptor
	frequency = getset_descriptor
	invalid = getset_descriptor
	invert = getset_descriptor
	level = getset_descriptor
	name = getset_descriptor
	neg_ticks = getset_descriptor
	owner = getset_descriptor
	pos_ticks = getset_descriptor
	positive = getset_descriptor
	def reset(*argv):
		"""reset()
Reset sensor internal state, effect depends on the type of sensor and settings.
The sensor is put in its initial state as if it was just activated."""

	skippedTicks = getset_descriptor
	status = getset_descriptor
	tap = getset_descriptor
	triggered = getset_descriptor
	useNegPulseMode = getset_descriptor
	usePosPulseMode = getset_descriptor

class SCA_AlwaysSensor:
	executePriority = getset_descriptor
	frequency = getset_descriptor
	invalid = getset_descriptor
	invert = getset_descriptor
	level = getset_descriptor
	name = getset_descriptor
	neg_ticks = getset_descriptor
	owner = getset_descriptor
	pos_ticks = getset_descriptor
	positive = getset_descriptor
	def reset(*argv):
		"""reset()
Reset sensor internal state, effect depends on the type of sensor and settings.
The sensor is put in its initial state as if it was just activated."""

	skippedTicks = getset_descriptor
	status = getset_descriptor
	tap = getset_descriptor
	triggered = getset_descriptor
	useNegPulseMode = getset_descriptor
	usePosPulseMode = getset_descriptor

class SCA_DelaySensor:
	delay = getset_descriptor
	duration = getset_descriptor
	executePriority = getset_descriptor
	frequency = getset_descriptor
	invalid = getset_descriptor
	invert = getset_descriptor
	level = getset_descriptor
	name = getset_descriptor
	neg_ticks = getset_descriptor
	owner = getset_descriptor
	pos_ticks = getset_descriptor
	positive = getset_descriptor
	repeat = getset_descriptor
	def reset(*argv):
		"""reset()
Reset sensor internal state, effect depends on the type of sensor and settings.
The sensor is put in its initial state as if it was just activated."""

	skippedTicks = getset_descriptor
	status = getset_descriptor
	tap = getset_descriptor
	triggered = getset_descriptor
	useNegPulseMode = getset_descriptor
	usePosPulseMode = getset_descriptor

class SCA_IController:
	actuators = getset_descriptor
	executePriority = getset_descriptor
	invalid = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	sensors = getset_descriptor
	state = getset_descriptor
	useHighPriority = getset_descriptor

class SCA_ILogicBrick:
	executePriority = getset_descriptor
	invalid = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor

class SCA_IObject:
	invalid = getset_descriptor
	name = getset_descriptor

class SCA_ISensor:
	executePriority = getset_descriptor
	frequency = getset_descriptor
	invalid = getset_descriptor
	invert = getset_descriptor
	level = getset_descriptor
	name = getset_descriptor
	neg_ticks = getset_descriptor
	owner = getset_descriptor
	pos_ticks = getset_descriptor
	positive = getset_descriptor
	def reset(*argv):
		"""reset()
Reset sensor internal state, effect depends on the type of sensor and settings.
The sensor is put in its initial state as if it was just activated."""

	skippedTicks = getset_descriptor
	status = getset_descriptor
	tap = getset_descriptor
	triggered = getset_descriptor
	useNegPulseMode = getset_descriptor
	usePosPulseMode = getset_descriptor

class SCA_InputEvent:
	invalid = getset_descriptor
	queue = getset_descriptor
	status = getset_descriptor
	type = getset_descriptor
	values = getset_descriptor

class SCA_JoystickSensor:
	axis = getset_descriptor
	axisSingle = getset_descriptor
	axisValues = getset_descriptor
	button = getset_descriptor
	connected = getset_descriptor
	executePriority = getset_descriptor
	frequency = getset_descriptor
	def getButtonActiveList(*argv):
		"""getButtonActiveList
Returns a list containing the indices of the button currently pressed."""

	def getButtonStatus(*argv):
		"""getButtonStatus(buttonIndex)
Returns a bool of the current pressed state of the specified button."""

	hat = getset_descriptor
	hatSingle = getset_descriptor
	hatValues = getset_descriptor
	index = getset_descriptor
	invalid = getset_descriptor
	invert = getset_descriptor
	level = getset_descriptor
	name = getset_descriptor
	neg_ticks = getset_descriptor
	numAxis = getset_descriptor
	numButtons = getset_descriptor
	numHats = getset_descriptor
	owner = getset_descriptor
	pos_ticks = getset_descriptor
	positive = getset_descriptor
	def reset(*argv):
		"""reset()
Reset sensor internal state, effect depends on the type of sensor and settings.
The sensor is put in its initial state as if it was just activated."""

	skippedTicks = getset_descriptor
	status = getset_descriptor
	tap = getset_descriptor
	threshold = getset_descriptor
	triggered = getset_descriptor
	useNegPulseMode = getset_descriptor
	usePosPulseMode = getset_descriptor

class SCA_KeyboardSensor:
	events = getset_descriptor
	executePriority = getset_descriptor
	frequency = getset_descriptor
	def getKeyStatus(*argv):
		"""getKeyStatus(keycode)
Get the given key's status (NONE, JUSTACTIVATED, ACTIVE or JUSTRELEASED)."""

	hold1 = getset_descriptor
	hold2 = getset_descriptor
	inputs = getset_descriptor
	invalid = getset_descriptor
	invert = getset_descriptor
	key = getset_descriptor
	level = getset_descriptor
	name = getset_descriptor
	neg_ticks = getset_descriptor
	owner = getset_descriptor
	pos_ticks = getset_descriptor
	positive = getset_descriptor
	def reset(*argv):
		"""reset()
Reset sensor internal state, effect depends on the type of sensor and settings.
The sensor is put in its initial state as if it was just activated."""

	skippedTicks = getset_descriptor
	status = getset_descriptor
	tap = getset_descriptor
	targetProperty = getset_descriptor
	toggleProperty = getset_descriptor
	triggered = getset_descriptor
	useAllKeys = getset_descriptor
	useNegPulseMode = getset_descriptor
	usePosPulseMode = getset_descriptor

class SCA_MouseSensor:
	executePriority = getset_descriptor
	frequency = getset_descriptor
	def getButtonStatus(*argv):
		"""getButtonStatus(button)
Get the given button's status (KX_INPUT_NONE, KX_INPUT_NONE, KX_INPUT_JUST_ACTIVATED, KX_INPUT_ACTIVE, KX_INPUT_JUST_RELEASED)."""

	invalid = getset_descriptor
	invert = getset_descriptor
	level = getset_descriptor
	mode = getset_descriptor
	name = getset_descriptor
	neg_ticks = getset_descriptor
	owner = getset_descriptor
	pos_ticks = getset_descriptor
	position = getset_descriptor
	positive = getset_descriptor
	def reset(*argv):
		"""reset()
Reset sensor internal state, effect depends on the type of sensor and settings.
The sensor is put in its initial state as if it was just activated."""

	skippedTicks = getset_descriptor
	status = getset_descriptor
	tap = getset_descriptor
	triggered = getset_descriptor
	useNegPulseMode = getset_descriptor
	usePosPulseMode = getset_descriptor

class SCA_NANDController:
	actuators = getset_descriptor
	executePriority = getset_descriptor
	invalid = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	sensors = getset_descriptor
	state = getset_descriptor
	useHighPriority = getset_descriptor

class SCA_NORController:
	actuators = getset_descriptor
	executePriority = getset_descriptor
	invalid = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	sensors = getset_descriptor
	state = getset_descriptor
	useHighPriority = getset_descriptor

class SCA_ORController:
	actuators = getset_descriptor
	executePriority = getset_descriptor
	invalid = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	sensors = getset_descriptor
	state = getset_descriptor
	useHighPriority = getset_descriptor

class SCA_PropertyActuator:
	executePriority = getset_descriptor
	invalid = getset_descriptor
	mode = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	propName = getset_descriptor
	value = getset_descriptor

class SCA_PropertySensor:
	executePriority = getset_descriptor
	frequency = getset_descriptor
	invalid = getset_descriptor
	invert = getset_descriptor
	level = getset_descriptor
	max = getset_descriptor
	min = getset_descriptor
	mode = getset_descriptor
	name = getset_descriptor
	neg_ticks = getset_descriptor
	owner = getset_descriptor
	pos_ticks = getset_descriptor
	positive = getset_descriptor
	propName = getset_descriptor
	def reset(*argv):
		"""reset()
Reset sensor internal state, effect depends on the type of sensor and settings.
The sensor is put in its initial state as if it was just activated."""

	skippedTicks = getset_descriptor
	status = getset_descriptor
	tap = getset_descriptor
	triggered = getset_descriptor
	useNegPulseMode = getset_descriptor
	usePosPulseMode = getset_descriptor
	value = getset_descriptor

class SCA_PythonController:
	def activate(*argv):
		pass

	actuators = getset_descriptor
	def deactivate(*argv):
		pass

	executePriority = getset_descriptor
	invalid = getset_descriptor
	mode = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	script = getset_descriptor
	sensors = getset_descriptor
	state = getset_descriptor
	useHighPriority = getset_descriptor

class SCA_PythonJoystick:
	activeButtons = getset_descriptor
	axisValues = getset_descriptor
	hatValues = getset_descriptor
	invalid = getset_descriptor
	name = getset_descriptor
	numAxis = getset_descriptor
	numButtons = getset_descriptor
	numHats = getset_descriptor

class SCA_PythonKeyboard:
	activeInputs = getset_descriptor
	active_events = getset_descriptor
	events = getset_descriptor
	def getClipboard(*argv):
		"""getCliboard doc"""

	inputs = getset_descriptor
	invalid = getset_descriptor
	def setClipboard(*argv):
		"""setCliboard doc"""

	text = getset_descriptor

class SCA_PythonMouse:
	activeInputs = getset_descriptor
	active_events = getset_descriptor
	events = getset_descriptor
	inputs = getset_descriptor
	invalid = getset_descriptor
	position = getset_descriptor
	visible = getset_descriptor

class SCA_RandomActuator:
	distribution = getset_descriptor
	executePriority = getset_descriptor
	invalid = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	para1 = getset_descriptor
	para2 = getset_descriptor
	propName = getset_descriptor
	seed = getset_descriptor
	def setBoolBernouilli(*argv):
		"""setBoolBernouilli(value)
- value: a float between 0 and 1
Return false value * 100%% of the time."""

	def setBoolConst(*argv):
		"""setBoolConst(value)
- value: 0 or 1
Set this generator to produce a constant boolean value."""

	def setBoolUniform(*argv):
		"""setBoolUniform()
Set this generator to produce true and false, each with 50%% chance of occurring"""

	def setFloatConst(*argv):
		"""setFloatConst(value)
- value: float
Always return value"""

	def setFloatNegativeExponential(*argv):
		"""setFloatNegativeExponential(half_life)
- half_life: float
Return negative-exponentially distributed numbers. The half-life 'time'
is characterized by half_life."""

	def setFloatNormal(*argv):
		"""setFloatNormal(mean, standard_deviation)
- mean: float
- standard_deviation: float
Return normal-distributed numbers. The average is mean, and the
deviation from the mean is characterized by standard_deviation."""

	def setFloatUniform(*argv):
		"""setFloatUniform(lower_bound, upper_bound)
- lower_bound: float
- upper_bound: float
Return a random integer between lower_bound and
upper_bound."""

	def setIntConst(*argv):
		"""setIntConst(value)
- value: integer
Always return value"""

	def setIntPoisson(*argv):
		"""setIntPoisson(value)
- value: float
Return a Poisson-distributed number. This performs a series
of Bernouilli tests with parameter value. It returns the
number of tries needed to achieve succes."""

	def setIntUniform(*argv):
		"""setIntUniform(lower_bound, upper_bound)
- lower_bound: integer
- upper_bound: integer
Return a random integer between lower_bound and
upper_bound. The boundaries are included."""


class SCA_RandomSensor:
	executePriority = getset_descriptor
	frequency = getset_descriptor
	invalid = getset_descriptor
	invert = getset_descriptor
	lastDraw = getset_descriptor
	level = getset_descriptor
	name = getset_descriptor
	neg_ticks = getset_descriptor
	owner = getset_descriptor
	pos_ticks = getset_descriptor
	positive = getset_descriptor
	def reset(*argv):
		"""reset()
Reset sensor internal state, effect depends on the type of sensor and settings.
The sensor is put in its initial state as if it was just activated."""

	seed = getset_descriptor
	skippedTicks = getset_descriptor
	status = getset_descriptor
	tap = getset_descriptor
	triggered = getset_descriptor
	useNegPulseMode = getset_descriptor
	usePosPulseMode = getset_descriptor

class SCA_VibrationActuator:
	duration = getset_descriptor
	executePriority = getset_descriptor
	invalid = getset_descriptor
	joyindex = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	strength = getset_descriptor

class SCA_XNORController:
	actuators = getset_descriptor
	executePriority = getset_descriptor
	invalid = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	sensors = getset_descriptor
	state = getset_descriptor
	useHighPriority = getset_descriptor

class SCA_XORController:
	actuators = getset_descriptor
	executePriority = getset_descriptor
	invalid = getset_descriptor
	name = getset_descriptor
	owner = getset_descriptor
	sensors = getset_descriptor
	state = getset_descriptor
	useHighPriority = getset_descriptor



