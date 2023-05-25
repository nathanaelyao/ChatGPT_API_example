def add(add1, add2):
    return add1 + add2

def uncompress( inputFile, outputFile ):
    
  # Check that it's a known file

  if inputFile.readline() != headerText + b'\n':
    sys.stderr.write( "Input is not in the '%s' format.\n" % headerText )
    sys.exit(1)
    
  # Read the rows, columns, and channels.  

  rows, columns, numChannels = [ int(x) for x in inputFile.readline().split() ]

  # Read the raw bytes.

  inputBytes = bytearray(inputFile.read())

  startTime = time.time()

  # ---------------- [YOUR CODE HERE] ----------------
  #
  # REPLACE THIS WITH YOUR OWN CODE TO CONVERT THE 'inputBytes' ARRAY INTO AN IMAGE IN 'img'.

  img = np.empty([rows,columns,numChannels], dtype=np.uint8)
  count = 0

  indices = []
  for i in range(0, len(inputBytes), 2):
    integer = struct.unpack('>H', inputBytes[i:i+2])[0]
    indices.append(integer)

  #dict to store codes
  dictionary = {}
  for i in range(-255,256):
    dictionary[i + 255] = struct.pack('>h', i)

  s = dictionary[indices[0]]
  out = [struct.unpack('>h', s)[0]]

  #decode with LZW
  for i in indices[1:]:
    #code already in dict
    if i in dictionary:
      tValue = dictionary[i]
      dictionary[len(dictionary)] = s + dictionary[i][0:2] # Add the new LZW code and its corresponding value to the dictionary
      s = dictionary[i]
    else:
      #not in dict
      tValue = s + s[0:2]
      dictionary[len(dictionary)] = s + s[0:2] # Add the new LZW code and its corresponding value to the dictionary
      s += s[0:2]
    for j in range(0, len(tValue), 2):
      # Convert the bytes to an integer
      pix = struct.unpack('>h',tValue[j:j+2])[0]+out[-1]
      out.append(pix)  

  # Loop over the rows, columns, and channels of the image and assign the values from the 'out' list to pixels
  for row in range(rows):
    for col in range(columns):
      for channel in range(numChannels):
        img[row][col][channel] = out[count]
        count+=1

