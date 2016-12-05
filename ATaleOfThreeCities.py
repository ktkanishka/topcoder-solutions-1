from decimal import Decimal

class ATaleOfThreeCities(object):
    def connect(self, ax, ay, bx, by, cx, cy):
        min_ab = float('inf')
        for a_index in xrange(len(ax)):
            for b_index in xrange(len(bx)):
                distance = ((Decimal(ax[a_index]) - Decimal(bx[b_index]))**2 +(Decimal(ay[a_index]) - Decimal(by[b_index]))**2 ).sqrt()
                if distance < min_ab:
                    min_ab = distance

        min_ac = float('inf')
        for a_index in xrange(len(ax)):
            for c_index in xrange(len(cx)):
                distance = ((Decimal(ax[a_index]) - Decimal(cx[c_index]))**2 +(Decimal(ay[a_index]) - Decimal(cy[c_index]))**2 ).sqrt()
                if distance < min_ac:
                    min_ac = distance
        
        min_bc = float('inf')
        for b_index in xrange(len(bx)):
            for c_index in xrange(len(cx)):
                distance = ((Decimal(bx[b_index]) - Decimal(cx[c_index]))**2 +(Decimal(by[b_index]) - Decimal(cy[c_index]))**2 ).sqrt()
                if distance < min_bc:
                    min_bc = distance

        return min(min_ab + min_ac, min_ab + min_bc, min_ac + min_bc)
