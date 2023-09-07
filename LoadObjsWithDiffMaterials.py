'''
    Demonstrates simple animation.
'''
import MaxPlus
import colorsys
import random
import os


# Function to generate a random saturated color in HSL format
def random_saturated_color_hsl():
    # Randomly choose a hue value between 0 and 1
    hue = random.random()
    # Set the saturation and lightness to a fixed value (you can adjust these)
    saturation = random.uniform(0.6, 0.8)  # saturation
    lightness = random.uniform(0.6, 0.8)  # lightness
    return (hue, saturation, lightness)
	
# Function to generate a random unsaturated color in HSL format
def random_unsaturated_color_hsl():
    # Randomly choose a hue value between 0 and 1
    hue = random.random()
    # Set the saturation and lightness to a fixed value (you can adjust these)
    saturation = random.uniform(0.8, 0.9)  # saturation
    lightness = random.uniform(0.4, 0.6)  # lightness
    return (hue, saturation, lightness)
	
# Function to convert HSL color to RGB color
def hsl_to_rgb(hsl):
    r, g, b = colorsys.hls_to_rgb(*hsl)
    return (r, g, b)
	
# generate 400 saturated colors for nodes
num_colors_node = 400
hsl_colors_node = [random_saturated_color_hsl() for _ in range(num_colors_node)]
rgb_colors_node = [hsl_to_rgb(hsl) for hsl in hsl_colors_node]

# generate 400 unsaturated colors for rods
num_colors_rod = 400
hsl_colors_rod = [random_unsaturated_color_hsl() for _ in range(num_colors_rod)]
rgb_colors_rod = [hsl_to_rgb(hsl) for hsl in hsl_colors_rod]

# Enter the folder path here
folderPath = os.getcwd()
#print folderPath
files = os.listdir(folderPath)
print files

i = 0
for fileName in files:
	
	if ".obj" not in fileName:
		continue
		
	print fileName
	#print MaxPlus.SelectionManager.GetCount()
		
	MaxPlus.FileManager.Import(fileName, True)
	
	currentObj = MaxPlus.SelectionManager.GetNode(0)
	
	currentObj.SetName(fileName)
	
	currentObj.Scale(MaxPlus.Point3(5, 5, 5))

	if "Node" in fileName:
		parts = fileName.split("_")
		currentLabel = int(parts[1])
		
		# Create current material
		currentColor = rgb_colors_node[currentLabel]
		print currentColor
		color = MaxPlus.Color(currentColor[0], currentColor[1], currentColor[2])
		
		m = MaxPlus.Factory.CreateDefaultStdMat()
		#m.Ambient = color
		m.Diffuse = color
		#m.Specular = MaxPlus.Color(1, 1, 1)
		m.Shininess = 0.5
		m.ShinyStrength = 0.7
		
		# Assign material to the current object
		currentObj.Material = m
		
	if "Rod" in fileName:
		parts = fileName.split("_")
		currentLabel = int(parts[1])
		
		# Create current material
		currentColor = rgb_colors_rod[currentLabel]
		print currentColor
		color = MaxPlus.Color(currentColor[0], currentColor[1], currentColor[2])
		
		m = MaxPlus.Factory.CreateDefaultStdMat()
		#m.Ambient = color
		m.Diffuse = color
		#m.Specular = MaxPlus.Color(1, 1, 1)
		#m.Shininess = 0.5
		#m.ShinyStrength = 0.7
		
		# Assign material to the current object
		currentObj.Material = m
		
	i = i + 1
		
	#print("Done. \n")
	
	#print currentObj.GetName()
#print rgb_colors_node
#print rgb_colors_rod

#~ print "Hello World Animation"
#~ doRedraw = True
#~ ticks = 160


#~ class PlaybackSpeed(object):
    #~ '''Enumerates the allowed values that can be passed to the
       #~ method Interface::SetPlaybackSpeed(int).'''
    #~ X1_4 = -4  # quarter time playback speed
    #~ X1_2 = -2  # half time playback speed
    #~ X1 = 1  # real time playback speed
    #~ X2 = 2  # double time playback speed
    #~ X4 = 4  # quadruple time playback speed


#~ def CreateSphere():
    #~ theSphere = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Sphere)
    #~ node = MaxPlus.Factory.CreateNode(theSphere)
    #~ return node


#~ def PrintInterval(interval):
    #~ '''This function prints an Interval instance nicely with identifiable values. i.e. 'Interval [0,100]'
       #~ It prints the values in terms of frames, instead of ticks.
       #~ Each frame contains 160 ticks. In the SDK, when Intervals are passed around, they
       #~ are not passed as the number of frames, but instead the frames multiplied by ticks (i.e. 160)'''
    #~ start = interval.Start() / 160
    #~ end = interval.End() / 160
    #~ print "Current Animation Range: [%d,%d]" % (start, end)


#~ def SetAnimationRanges():
    #~ '''Changes the animation range from the default of 100 frames to 200 frames'''
    #~ anim = MaxPlus.Animation
    #~ PrintInterval(anim.GetAnimRange())
    #~ # Intervals come in units of ticks. Each frame is 160 ticks.
    #~ newFrames = 200 * 160
    #~ newRange = MaxPlus.Interval(0, newFrames)
    #~ anim.SetRange(newRange)
    #~ # The animation slider now shows 200 frames
    #~ PrintInterval(anim.GetAnimRange())


#~ def AnimateTransform(sphere):
    #~ '''Moves the sphere around to demonstrate animation'''
    #~ # select the sphere so we will see the keyframes in the timeslider
    #~ sphere.Select()
    #~ anim = MaxPlus.Animation
    #~ # Turn on the AutoKey button
    #~ anim.SetAnimateButtonState(True)

    #~ # Now create some keyframes
    #~ # Advanced the time slider to frame 30
    #~ anim.SetTime(30 * ticks, doRedraw)
    #~ # Move the sphere, this creates a keyframe
    #~ sphere.Move(MaxPlus.Point3(50, 0, 0))

    #~ anim.SetTime(60 * ticks, doRedraw)
    #~ sphere.Move(MaxPlus.Point3(50, 50, 0))

    #~ anim.SetTime(90 * ticks, doRedraw)
    #~ sphere.Move(MaxPlus.Point3(-50, 50, 0))

    #~ anim.SetTime(120 * ticks, doRedraw)
    #~ sphere.Move(MaxPlus.Point3(-50, 0, 0))

    #~ anim.SetTime(150 * ticks, doRedraw)
    #~ sphere.Move(MaxPlus.Point3(-50, -50, 0))

    #~ anim.SetTime(180 * ticks, doRedraw)
    #~ sphere.Move(MaxPlus.Point3(50, -50, 0))  # moves back to the origin

    #~ # Turn off the AutoKey button
    #~ anim.SetAnimateButtonState(False)


#~ def PlaybackAnimation(sphere):
    #~ '''There are two StartPlayback methods. One takes a boolean value,
       #~ and the other takes an integer.
       #~ The function that takes a boolean value immediately returns.
       #~ Thus execution is delayed until after the python script is completed.
       #~ The function that takes an integer (1 for TRUE) does not return
       #~ until all playback is completed.
       #~ Attempting to call anim.StartPlayback with the boolean overload
       #~ will produce confusing results and is best avoided.'''
    #~ anim = MaxPlus.Animation
    #~ # The timeslider was last set to 180. But the total time range is 200
    #~ # This will play back only 20 frames worth of animation and then stop at
    #~ # frame 200
    #~ print "Playing back Animation first time"
    #~ anim.SetPlaybackLoop(False)
    #~ OldStyle = 1
    #~ # The old style plays back the animation and does not immediately return
    #~ anim.StartPlayback(OldStyle)  # ends at frame 200

    #~ print "Playing back Animation second time"
    #~ # now rewind the time slider back to frame 0
    #~ anim.SetTime(0 * ticks, doRedraw)
    #~ # and now play back the entire sequence from frame 0 to 200.
    #~ anim.StartPlayback(OldStyle)

    #~ # Change the playback speed
    #~ print "Playing back Animation third time"
    #~ anim.SetTime(0 * ticks, doRedraw)
    #~ anim.SetPlaybackSpeed(PlaybackSpeed.X4)
    #~ anim.StartPlayback(OldStyle)


#~ def DemoAnimation():
    #~ MaxPlus.FileManager.Reset(True)
    #~ sphere = CreateSphere()
    #~ SetAnimationRanges()
    #~ AnimateTransform(sphere)
    #~ PlaybackAnimation(sphere)

#~ DemoAnimation()
