"""
Gitter

- Schaffst du es mit einem zweiten Loop ein Gittermuster 
  herzustellen?
"""

newPage(300, 300)

for i in range(0, width(), 10): 
    stroke(0)
    line((i,0),(i, width()))
    
for i in range(0, width(), 10): 
    stroke(0)
    line((0,i),(width(),i))
