class LpCalculator:
    def __init__(self, main_curr=100, base_curr=100, decimal=1):
        self.main_curr = main_curr
        self.res_main_curr = 0
        self.base_curr = base_curr
        self.res_base_curr = 0
        self.k = self.main_curr * self.base_curr
        self.decimal = decimal

    def print_lp(self):
        main_curr = round(self.main_curr / self.decimal, 3)
        res_main_curr = round(self.res_main_curr / self.decimal, 3)
        base_curr = round(self.base_curr / self.decimal, 3)
        res_base_curr = round(self.res_base_curr / self.decimal, 3)
        print(f"{main_curr=}, {res_main_curr=}, curr1_total={main_curr+res_main_curr}\n"
              f"{base_curr=}, {res_base_curr=}, curr2_total={base_curr+res_base_curr}\n"
              f"total={main_curr+res_main_curr+base_curr+res_base_curr}")

    def update_lp_by_req_ratio(self, req_ratio=1.05):
        """req_ratio is the final ratio which LP should have after it is updated."""
        self.main_curr = (self.k / req_ratio) ** 0.5
        self.base_curr = self.main_curr * req_ratio

    def update_lp_by_change_ratio(self, change_ratio=1.05):
        """change_ratio is the ratio by which you want to change the LP."""
        self.base_curr = (change_ratio * self.base_curr * self.k / self.main_curr) ** 0.5
        self.main_curr = self.k / self.base_curr

    def break_lp(self, break_pct=0.025, lp_conv_to_curr1=0.0, lp_conv_to_curr2=0.025):
        curr1_break = self.main_curr * break_pct
        curr2_break = self.base_curr * break_pct
        curr1_lp_conv_to_curr1 = self.main_curr * lp_conv_to_curr1
        curr2_lp_conv_to_curr1 = self.base_curr * lp_conv_to_curr1
        curr1_lp_conv_to_curr2 = self.main_curr * lp_conv_to_curr2
        curr2_lp_conv_to_curr2 = self.base_curr * lp_conv_to_curr2

        self.res_main_curr += curr1_break + curr1_lp_conv_to_curr1 + (curr2_lp_conv_to_curr1 * self.main_curr / self.base_curr)
        self.res_base_curr += curr2_break + curr2_lp_conv_to_curr2 + (curr1_lp_conv_to_curr2 * self.base_curr / self.main_curr)

        self.main_curr -= (curr1_break + curr1_lp_conv_to_curr1 + curr1_lp_conv_to_curr2)
        self.base_curr -= (curr2_break + curr2_lp_conv_to_curr1 + curr2_lp_conv_to_curr2)
        self.k = self.main_curr * self.base_curr

    def convert_and_add_main_curr_to_lp(self, main_curr):
        half_main_curr = main_curr / 2
        base_curr_added = half_main_curr * self.base_curr / self.main_curr
        self.main_curr += half_main_curr
        self.base_curr += base_curr_added
        self.k = self.main_curr * self.base_curr


def print_end():
    lp_calculator = LpCalculator(1407, 1676)
    lp_calculator.print_lp()
    lp_ratio = 1
    for i in range(25):
        lp_ratio *= 0.9
        print(f"{i=}, {lp_ratio=}")
        lp_calculator.update_lp_by_req_ratio(lp_ratio)
        lp_calculator.print_lp()
        lp_calculator.break_lp(0.1, 0.0, 0.0)
        lp_calculator.print_lp()
        print("")


def main():
    # print_end()
    lp_calculator = LpCalculator(400, 400)
    lp_calculator.print_lp()
    lp_calculator.update_lp_by_req_ratio(2)
    lp_calculator.print_lp()
    # lp_calculator.break_lp(0.05, 0.0, 0.0)
    # lp_calculator.print_lp()
    # lp_calculator.update_lp_by_req_ratio(1)
    # lp_calculator.print_lp()
    breakpoint()


if __name__ == '__main__':
    main()
