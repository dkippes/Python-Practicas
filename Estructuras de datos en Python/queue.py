
# FIFO
from collections import deque

# Listas como colas
queue = [1, , 2, 3]

queue.append(4)
queue.append(5)

queue.pop(0)
queue.pop(0)

# Colas implementadas eficientemente en la libreria estandar

queue = deque([1, , 2, 3])

# Agrego los elementos
queue.append(4)
queue.append(5)

# Saco los elementos
queue.popleft()
queue.popleft()
