'''This module provides access to the GLSL shader and Offscreen rendering functionalities.'''

CD_MCOL = int
CD_MTFACE = int
CD_ORCO = int
CD_TANGENT = int
GPU_DATA_16F = int
GPU_DATA_1F = int
GPU_DATA_1I = int
GPU_DATA_2F = int
GPU_DATA_3F = int
GPU_DATA_4F = int
GPU_DATA_4UB = int
GPU_DATA_9F = int
GPU_DYNAMIC_AMBIENT_COLOR = int
GPU_DYNAMIC_GROUP_LAMP = int
GPU_DYNAMIC_GROUP_MAT = int
GPU_DYNAMIC_GROUP_MISC = int
GPU_DYNAMIC_GROUP_MIST = int
GPU_DYNAMIC_GROUP_OBJECT = int
GPU_DYNAMIC_GROUP_SAMPLER = int
GPU_DYNAMIC_GROUP_WORLD = int
GPU_DYNAMIC_HORIZON_COLOR = int
GPU_DYNAMIC_LAMP_ATT1 = int
GPU_DYNAMIC_LAMP_ATT2 = int
GPU_DYNAMIC_LAMP_DISTANCE = int
GPU_DYNAMIC_LAMP_DYNCO = int
GPU_DYNAMIC_LAMP_DYNCOL = int
GPU_DYNAMIC_LAMP_DYNENERGY = int
GPU_DYNAMIC_LAMP_DYNIMAT = int
GPU_DYNAMIC_LAMP_DYNPERSMAT = int
GPU_DYNAMIC_LAMP_DYNSPOTSCALE = int
GPU_DYNAMIC_LAMP_DYNVEC = int
GPU_DYNAMIC_LAMP_SPOTBLEND = int
GPU_DYNAMIC_LAMP_SPOTSIZE = int
GPU_DYNAMIC_MAT_ALPHA = int
GPU_DYNAMIC_MAT_AMB = int
GPU_DYNAMIC_MAT_DIFFRGB = int
GPU_DYNAMIC_MAT_EMIT = int
GPU_DYNAMIC_MAT_HARD = int
GPU_DYNAMIC_MAT_MIR = int
GPU_DYNAMIC_MAT_REF = int
GPU_DYNAMIC_MAT_SPEC = int
GPU_DYNAMIC_MAT_SPECRGB = int
GPU_DYNAMIC_MAT_SPECTRA = int
GPU_DYNAMIC_MIST_COLOR = int
GPU_DYNAMIC_MIST_DISTANCE = int
GPU_DYNAMIC_MIST_ENABLE = int
GPU_DYNAMIC_MIST_INTENSITY = int
GPU_DYNAMIC_MIST_START = int
GPU_DYNAMIC_MIST_TYPE = int
GPU_DYNAMIC_NONE = int
GPU_DYNAMIC_OBJECT_AUTOBUMPSCALE = int
GPU_DYNAMIC_OBJECT_COLOR = int
GPU_DYNAMIC_OBJECT_IMAT = int
GPU_DYNAMIC_OBJECT_LOCTOVIEWIMAT = int
GPU_DYNAMIC_OBJECT_LOCTOVIEWMAT = int
GPU_DYNAMIC_OBJECT_MAT = int
GPU_DYNAMIC_OBJECT_VIEWIMAT = int
GPU_DYNAMIC_OBJECT_VIEWMAT = int
GPU_DYNAMIC_SAMPLER_2DBUFFER = int
GPU_DYNAMIC_SAMPLER_2DIMAGE = int
GPU_DYNAMIC_SAMPLER_2DSHADOW = int
GPU_DYNAMIC_TEX_ALPHA = int
GPU_DYNAMIC_TEX_COLFAC = int
GPU_DYNAMIC_TEX_COLINTENS = int
GPU_DYNAMIC_TEX_EMIT = int
GPU_DYNAMIC_TEX_HARDNESS = int
GPU_DYNAMIC_TEX_IOR = int
GPU_DYNAMIC_TEX_MIRROR = int
GPU_DYNAMIC_TEX_NORMAL = int
GPU_DYNAMIC_TEX_PARALLAXBUMP = int
GPU_DYNAMIC_TEX_PARALLAXSTEP = int
GPU_DYNAMIC_TEX_REFRRATIO = int
GPU_DYNAMIC_TEX_SPECFAC = int
GPU_DYNAMIC_TEX_SPECINTENS = int
GPU_DYNAMIC_ZENITH_COLOR = int
def export_shader(*argv):
	'''export_shader(scene, material)

Returns the GLSL shader that produces the visual effect of material in scene.

:return: Dictionary defining the shader, uniforms and attributes.
:rtype: Dict'''

import offscreen

