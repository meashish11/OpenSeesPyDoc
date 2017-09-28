import os.path

names = ["uniaxialMaterial", 
         "testUniaxialMaterial", 
         "setStrain", 
         "getStrain", 
         "getStress", 
         "getTangent", 
         "getDampTangent", 
         "wipe", 
         "model", 
         "node", 
         "fix", 
         "element", 
         "timeSeries", 
         "pattern", 
         "load", 
         "system", 
         "numberer", 
         "constraints", 
         "integrator", 
         "algorithm", 
         "analysis", 
         "analyze", 
         "nodeDisp", 
         "test", 
         "section", 
         "fiber", 
         "patch", 
         "layer", 
         "geomTransf", 
         "beamIntegration", 
         "loadConst", 
         "eleLoad", 
         "reactions", 
         "nodeReaction", 
         "eigen", 
         "nDMaterial", 
         "block2D", 
         "block3D", 
         "rayleigh", 
         "wipeAnalysis", 
         "setTime", 
         "remove", 
         "mass", 
         "equalDOF", 
         "nodeEigenvector", 
         "getTime", 
         "eleResponse", 
         "sp", 
         "fixX", 
         "fixY", 
         "fixZ", 
         "reset", 
         "initialize", 
         "getLoadFactor", 
         "build", 
         "Print", 
         "printA", 
         "printB", 
         "printGID", 
         "getCTestNorms", 
         "getCTestIter", 
         "recorder", 
         "database", 
         "save", 
         "restore", 
         "eleForce", 
         "eleDynamicalForce", 
         "nodeUnbalance", 
         "nodeVel", 
         "setNodeVel", 
         "setNodeDisp", 
         "nodeAccel", 
         "nodeResponse", 
         "nodeCoord", 
         "setNodeCoord", 
         "updateElementDomain", 
         "eleNodes", 
         "nodeMass", 
         "nodePressure", 
         "nodeBounds", 
         "start", 
         "stop", 
         "modalDamping", 
         "modalDampingQ", 
         "setElementRayleighDampingFactors", 
         "region", 
         "setPrecision", 
         "searchPeerNGA", 
         "domainChange", 
         "record", 
         "metaData", 
         "neesUpload", 
         "stripXML", 
         "convertBinaryToText", 
         "convertTextToBinary", 
         "getEleTags", 
         "getNodeTags", 
         "getParamTags", 
         "getParamValue", 
         "sectionForce", 
         "sectionDeformation", 
         "sectionStiffness", 
         "sectionFlexibility", 
         "sectionLocation", 
         "sectionWeight", 
         "basicDeformation", 
         "basicForce", 
         "basicStiffness", 
         "InitialStateAnalysis", 
         "totalCPU", 
         "solveCPU", 
         "accelCPU", 
         "numFact", 
         "numIter", 
         "systemSize", 
         "version", 
         "setMaxOpenFiles", 
         "background", 
         "limitCurve", 
         "imposedMotion", 
         "imposedSupportMotion", 
         "groundMotion", 
         "equalDOF_Mixed",
         "rigidLink", 
         "rigidDiaphragm", 
         "ShallowFoundationGen", 
         "setElementRayleighFactors", 
         "mesh", 
         "remesh", 
         "parameter", 
         "addToParameter", 
         "updateParameter"]


for name in names:

    if os.path.isfile(name+'.rst'):
        continue

    with open(name+'.rst', 'w') as f:

        f.write(name)
        f.write('\n')
        f.write('='*len(name))
    


snames = sorted(names, key=str.lower)
        
for name in snames:
    print(name)

    
