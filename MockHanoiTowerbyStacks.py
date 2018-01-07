class Tower:
    """
    @param: i: An integer from 0 to 2
    """
    def __init__(self, i):
        # create three towers
        self.disks = []

    """
    @param: d: An integer
    @return: nothing
    """
    def add(self, d):
        # Add a disk into this tower
        if len(self.disks) > 0 and self.disks[-1] <= d:
            print ("Error placing disk %s" % d)
        else:
            self.disks.append(d)

    """
    @param: t: a tower
    @return: nothing
    """
    def moveTopTo(self, t):
        # Move the top disk of this tower to the top of t.
        if len(self.disks) > 0:
            t.disks.append(self.disks.pop())

    """
    @param: n: An integer
    @param: destination: a tower
    @param: buffer: a tower
    @return: nothing
    """
    def move_disks(self, n, destination, buffer):
        # Move n Disks from this tower to destination by buffer tower
        if n == 0:
            return
        elif n == 1:
            self.moveTopTo(destination)
        else:
            self.move_disks(n-1, buffer, destination)
            self.moveTopTo(destination)
            buffer.move_disks(n-1, destination, self)

    """
    @return: Disks
    """
    def getDisks(self):
        # write your code here
        return self.disks

n = 6
towers = [Tower(0), Tower(1), Tower(2)]
for i in range(n - 1, -1, -1):
    towers[0].add(i)
towers[0].move_disks(n, towers[2], towers[1])
print (towers[0].disks, towers[1].disks, towers[2].disks)

"""
Your Tower object will be instantiated and called as such:
towers = [Tower(0), Tower(1), Tower(2)]
for i in xrange(n - 1, -1, -1): towers[0].add(i)
towers[0].move_disks(n, towers[2], towers[1])
print towers[0], towers[1], towers[2]
"""