class RangeMapper:
    def __init__(self, low, high, low_out=0.0, high_out=1.0):
        if high <= low:
            raise ValueError("High limit must be greater than low limit.")
        if high_out <= low_out:
            raise ValueError("High output limit must be greater than low output limit.")

        self.in_range = [low, high]
        self.out_range = [low_out, high_out]

    def get_input_range(self):
        if not self.in_range:
            raise ValueError("Input range is empty.")
        return self.in_range

    def get_output_range(self):
        if not self.out_range:
            raise ValueError("Output range is empty.")
        return self.out_range

    def map(self, to_map):
        derivative = (to_map - self.in_range[0]) / (self.in_range[1] - self.in_range[0])
        answer = self.out_range[0] + (self.out_range[1] - self.out_range[0]) * derivative

        if answer > self.out_range[1]:
            answer = self.out_range[1]
        if answer < self.out_range[0]:
            answer = self.out_range[0]
        
        return answer


class CharRangeMapper(RangeMapper):
    def __init__(self, low, high, low_out=0.0, high_out=1.0):
        self.alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        super().__init__(self.convert_to_range(low), self.convert_to_range(high), low_out, high_out)

    def map(self, to_map):
        return super().map(self.convert_to_range(to_map))

    def convert_to_range(self, cvt):
        c = cvt.upper()
        pos = self.alpha.find(c)
        if 0 <= pos <= 25:
            return pos + 1
        else:
            return 999
