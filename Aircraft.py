from math import sqrt
#Incomplete.
class Aircraft(object):
    def nearMiss(self, p1, v1, p2, v2, R):
        x = p2[0] - p1[0]
        y = p2[1] - p1[1]
        z = p2[2] - p1[2]
        vx = v2[0] - v1[0]
        vy = v2[1] - v1[1]
        vz = v2[2] - v1[2]
        a = vx + vy + vz
        b = 2 * (x * vx + y * vy + z * vz)
        c = x ** 2 + y ** 2 + z ** 2 + R ** 2
        try:
            s = sqrt(b**2 - 4*a*c)
            if (-b + s)/(2*a) >= 0:
                return "YES"
            elif (-b - s)/(s * a) >= 0:
                return "YES"
            else:
                return "NO"
        except ValueError as e:
            return "NO"
