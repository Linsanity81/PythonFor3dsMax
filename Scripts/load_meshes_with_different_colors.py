import colorsys
import random
import os
import pymxs
import numpy as np
from pymxs import runtime as rt 

random.seed(10)

# Function to generate a random saturated color in HSL format
def random_saturated_color_hsl():
    # Randomly choose a hue value between 0 and 1
    hue = random.random()
    # Set the saturation and lightness to a fixed value (you can adjust these)
    saturation = random.uniform(0.4, 0.6)  # saturation
    lightness = random.uniform(0.8, 0.9)  # lightness
    return (hue, saturation, lightness)
	
# Function to generate a random unsaturated color in HSL format
def random_unsaturated_color_hsl():
    # Randomly choose a hue value between 0 and 1
    hue = random.random()
    # Set the saturation and lightness to a fixed value (you can adjust these)
    saturation = random.uniform(0.4, 0.6)  # saturation
    lightness = random.uniform(0.4, 0.6)  # lightness
    return (hue, saturation, lightness)
	
# Function to convert HSL color to RGB color
def hsl_to_rgb(hsl):
    r, g, b = colorsys.hls_to_rgb(*hsl)
    return (r, g, b)
	
# generate 400 saturated colors for nodes
num_colors_node = 400
rgb_colors_node = []

rgb_colors_node.append((236/ 255.0, 82/ 255.0, 21/ 255.0))
rgb_colors_node.append((20/ 255.0, 100/ 255.0, 240/ 255.0))
rgb_colors_node.append((18/ 255.0, 190/ 255.0, 99/ 255.0))
rgb_colors_node.append((82/ 255.0, 16/ 255.0, 221/ 255.0))
rgb_colors_node.append((240/ 255.0, 240/ 255.0, 40/ 255.0))

rgb_colors_node.append((157/ 255.0, 57/ 255.0, 235/ 255.0))
rgb_colors_node.append((160/ 255.0, 242/ 255.0, 26/ 255.0))
rgb_colors_node.append((203/ 255.0, 13/ 255.0, 120/ 255.0))
rgb_colors_node.append((19/ 255.0, 236/ 255.0, 211/ 255.0))

rgb_colors_node.append((30/ 255.0, 34/ 255.0, 211/ 255.0))
rgb_colors_node.append((30/ 255.0, 237/ 255.0, 93/ 255.0))
rgb_colors_node.append((228/ 255.0, 193/ 255.0, 30/ 255.0))
rgb_colors_node.append((221/ 255.0, 19/ 255.0, 33/ 255.0))
rgb_colors_node.append((62/ 255.0, 183/ 255.0, 234/ 255.0))

rgb_colors_node.append((155/ 255.0, 100/ 255.0, 80/ 255.0))

while (len(rgb_colors_node) < num_colors_node):
	currentColorHSL = random_saturated_color_hsl()
	currentColorRGB = hsl_to_rgb(currentColorHSL)
	#print currentColorRGB
		
	for color_node in rgb_colors_node:
		if (abs(currentColorRGB[0] - color_node[0]) >= 0.1) or (abs(currentColorRGB[1] - color_node[1]) >= 0.1) or (abs(currentColorRGB[2] - color_node[2]) >= 0.1):
			rgb_colors_node.append(currentColorRGB)
			#print "add successfully"
			break
	
#~ num_colors_node = 400 
#~ hsl_colors_node = [random_saturated_color_hsl() for _ in range(num_colors_node)]
#~ rgb_colors_node = [hsl_to_rgb(hsl) for hsl in hsl_colors_node]

# generate 400 unsaturated colors for rods
num_colors_rod = 400
rgb_colors_rod = []
rgb_colors_rod.append((155/ 255.0, 155/ 255.0, 230/ 255.0))
rgb_colors_rod.append((100/ 255.0, 230/ 255.0, 100/ 255.0))
rgb_colors_rod.append((230/ 255.0, 155/ 255.0, 100/ 255.0))
rgb_colors_rod.append((230/ 255.0, 130/ 255.0, 130/ 255.0))
rgb_colors_rod.append((230/ 255.0, 230/ 255.0, 130/ 255.0))

rgb_colors_rod.append((180/ 255.0, 130/ 255.0, 230/ 255.0))
rgb_colors_rod.append((100/ 255.0, 230/ 255.0, 230/ 255.0))
rgb_colors_rod.append((230/ 255.0, 130/ 255.0, 190/ 255.0))
rgb_colors_rod.append((155/ 255.0, 220/ 255.0, 80/ 255.0))
rgb_colors_rod.append((108/ 255.0, 246/ 255.0, 203/ 255.0))

rgb_colors_rod.append((190/ 255.0, 97/ 255.0, 201/ 255.0))
rgb_colors_rod.append((100/ 255.0, 200/ 255.0, 180/ 255.0))
rgb_colors_rod.append((155/ 255.0, 155/ 255.0, 80/ 255.0))

while (len(rgb_colors_rod) < num_colors_node):
	currentColorHSL = random_unsaturated_color_hsl()
	currentColorRGB = hsl_to_rgb(currentColorHSL)
	
	for color_rod in rgb_colors_rod:
		if (abs(currentColorRGB[0] - color_rod[0]) >= 0.1) or (abs(currentColorRGB[1] - color_rod[1]) >= 0.1) or (abs(currentColorRGB[2] - color_rod[2]) >= 0.1):
			rgb_colors_rod.append(currentColorRGB)
			break
            
#~ folderPath = os.getcwd()
#~ files = os.listdir(folderPath)

#~ nodeBucket = np.zeros(1000)
#~ rodBucket = np.zeros(1000)
#~ sequence_node = np.zeros(1000)
#~ sequence_rod = np.zeros(1000)

#~ for fileName in files:
    
    #~ if ".obj" not in fileName:
        #~ continue
        
    #~ if "Node" in fileName:
        #~ nameOnly = fileName.split(".")
        #~ parts = nameOnly[0].split("_")
        #~ currentLabel = int(parts[1])
        #~ nodeBucket[currentLabel] = nodeBucket[currentLabel] + 1
        
    #~ if "Rod" in fileName:
        #~ nameOnly = fileName.split(".")
        #~ parts = nameOnly[0].split("_")
        #~ currentLabel = int(parts[1])
        #~ rodBucket[currentLabel] = rodBucket[currentLabel] + 1
        
#~ i = 1
#~ while (np.max(nodeBucket) > 0):
    
    #~ currentIndex = np.argmax(nodeBucket)
    
    #~ #print(currentIndex)
    
    #~ nodeBucket[currentIndex] = 0
    
    #~ sequence_node[currentIndex] = i
    
    #~ i = i + 1
    
#~ i = 1
#~ while (np.max(rodBucket) > 0):
    
    #~ currentIndex = np.argmax(rodBucket)
    
    #~ rodBucket[currentIndex] = 0
    
    #~ sequence_rod[currentIndex] = i
    
    #~ i = i + 1
    
#~ node_index = 1
#~ rod_index = 1
#~ for fileName in files:
    #~ if ".obj" not in fileName:
        #~ continue
        
    #~ if "Node" in fileName:
        #~ nameOnly = fileName.split(".")
        #~ parts = nameOnly[0].split("_")
        #~ currentLabel = int(parts[1])
        #~ os.rename(fileName, "myNode_" + str(int(sequence_node[currentLabel])) + "_" + str(node_index) + ".obj"  )
        #~ node_index = node_index + 1
        
    #~ if "Rod" in fileName:
        #~ nameOnly = fileName.split(".")
        #~ parts = nameOnly[0].split("_")
        #~ currentLabel = int(parts[1])
        #~ os.rename(fileName, "myRod_" + str(int(sequence_rod[currentLabel])) + "_" + str(rod_index) + ".obj"  )
        #~ rod_index = rod_index + 1

#~ print(files)

folderPath = os.getcwd()
files = os.listdir(folderPath)

i = 0
for fileName in files:
    
    if ".obj" not in fileName:
        continue
        
    pymxs.runtime.importFile(fileName, rt.readvalue(rt.StringStream('#noPrompt')))
    
    currentObj = rt.getCurrentSelection()[0]
    
    currentObj.name = fileName
    
    currentObj.scale = rt.Point3(5, 5, 5)
    
    if "Node" in fileName:
        nameOnly = fileName.split(".")
        parts = nameOnly[0].split("_")
        currentLabel = int(parts[1])
        
        currentColor = rgb_colors_node[currentLabel - 1]
        
        color = rt.Color(currentColor[0] * 255.0, currentColor[1] * 255.0, currentColor[2] * 255.0)
        
        m = rt.StandardMaterial()
        
        m.Diffuse = color
        m.Specular = rt.color(255,255,255)
        m.Shininess = 80
        m.Specular_Level = 100
        m.ShinyStrength = 80
        m.Glossiness = 60
        m.Name = fileName
        
        currentObj.Material = m
        
    if "Rod" in fileName:
        nameOnly = fileName.split(".")
        parts = nameOnly[0].split("_")
        currentLabel = int(parts[1])
        
        currentColor = rgb_colors_rod[currentLabel - 1]
        
        color = rt.Color(currentColor[0] * 255.0, currentColor[1] * 255.0, currentColor[2] * 255.0)
         
        m = rt.StandardMaterial()
        
        m.Diffuse = color
        m.Specular = rt.color(255,255,255)
        m.Shininess = 0
        m.ShinyStrength = 0
        m.Name = fileName
        
        currentObj.Material = m
        
