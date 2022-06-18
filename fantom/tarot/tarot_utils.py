def calculate_borrow_amount_converted_to_lp_to_required_borrow_pct(curr_in_collateral, borrow_amount,
                                                                   required_borrow_pct):
    """Borrow x TShare, and convert x/2 TShare to ftm and then create LP."""
    return int((required_borrow_pct * ((2*curr_in_collateral) - borrow_amount)) - (2*curr_in_collateral))


def calculate_borrow_amount_converted_to_half_lp_to_required_borrow_pct(
        curr_in_collateral, borrow_amount, required_borrow_pct):
    """Borrow x Tshare, and add same amount of FTM (from our side) and convert to LP"""
    new_collateral = required_borrow_pct*(2*curr_in_collateral - 2*borrow_amount)/(2-required_borrow_pct)
    return int((new_collateral - 2*curr_in_collateral)/2)


def calculate_borrow_amount_to_required_borrow_pct(curr_in_collateral, borrow_amount, required_borrow_pct):
    assert curr_in_collateral > 0
    borrow_required = (2 * curr_in_collateral) * (1 - (1 / required_borrow_pct)) - borrow_amount
    return int(borrow_required)


def get_tokens_required_to_reduce_borrow_pct(curr_amount, current_borrow_pct, required_borrow_pct):
    # ToDo
    raise NotImplementedError


def calculate_current_borrow_pct(curr_in_collateral, borrow_amount):
    assert curr_in_collateral > 0
    return round((2*curr_in_collateral) / ((2*curr_in_collateral) - borrow_amount), 3)


def calculate_current_borrow_amount(curr_in_collateral, borrow_pct):
    assert curr_in_collateral > 0
    return int(2*curr_in_collateral*(borrow_pct - 1)/borrow_pct)


def calculate_current_collateral(borrow_pct, borrow_amount):
    return int(borrow_pct * borrow_amount / (borrow_pct - 1))


def calculate_current_main_curr_in_collateral(borrow_pct, borrow_amount):
    return int(calculate_current_collateral(borrow_pct, borrow_amount) / 2)


def calculate_total_borrow_pct(main_curr_in_collateral, base_curr_in_collateral,
                               main_borrow_amount, base_borrow_amount):
    main_borrow_in_base_denomination = main_borrow_amount * base_curr_in_collateral / main_curr_in_collateral
    total_borrow = main_borrow_in_base_denomination + base_borrow_amount
    total_borrow_pct = calculate_current_borrow_pct(base_curr_in_collateral, total_borrow)
    return round(total_borrow_pct, 3)


# def calculate_total_borrow_pct(main_curr_in_collateral, base_curr_in_collateral,
#                                main_borrow_amount, base_borrow_amount):
#     """This was incorrect"""
#     main_borrow_pct = calculate_current_borrow_pct(main_curr_in_collateral/2, main_borrow_amount)
#     base_borrow_pct = calculate_current_borrow_pct(base_curr_in_collateral/2, base_borrow_amount)
#     return round((main_borrow_pct + base_borrow_pct) / 2, 3)


def calculate_main_and_base_borrow_for_leverage(main_curr_in_collateral, base_curr_in_collateral,
                                                main_borrow_amount, base_borrow_amount, leverage):
    """main_curr_in_collateral is in main_curr denomination and
    base_curr_in_collateral is in base_curr denomination."""
    total_base_curr_in_collateral = get_total_base_curr(
        main_curr_in_collateral, base_curr_in_collateral, 0, 0)
    total_base_curr = get_total_base_curr(main_curr_in_collateral, base_curr_in_collateral,
                                          main_borrow_amount, base_borrow_amount)
    total_base_borrow = total_base_curr_in_collateral - total_base_curr
    additional_req_borrow = calculate_borrow_amount_converted_to_lp_to_required_borrow_pct(
        total_base_curr_in_collateral/2, total_base_borrow, leverage)
    # breakpoint()
    # additional_req_borrow = total_req_base_borrow - total_base_borrow
    additional_base_borrow = int(additional_req_borrow / 2)
    additional_main_borrow = int((additional_req_borrow / 2) * (main_curr_in_collateral / base_curr_in_collateral))
    return additional_main_borrow, additional_base_borrow


def get_total_base_curr(main_curr_in_collateral, base_curr_in_collateral, main_borrow_amount, base_borrow_amount):
    """main_curr_in_collateral is in main_curr denomination and
    base_curr_in_collateral is in base_curr denomination."""
    main_curr = main_curr_in_collateral - main_borrow_amount
    base_curr = base_curr_in_collateral - base_borrow_amount
    total_base_curr = base_curr + (main_curr * base_curr_in_collateral / main_curr_in_collateral)
    return int(total_base_curr)


def calculate_borrow_amount_for_lp_and_staking_to_required_pct(
        curr_in_collateral, main_borrow_amount, lp_borrow_pct, total_borrow_pct):
    """Bx: main_curr, Bs: main_curr,
    Borrow Bx and convert it to LP and stake on tarot, then borrow Bs amount and take it to other website."""
    lp_borrow_amount = calculate_borrow_amount_converted_to_lp_to_required_borrow_pct(
        curr_in_collateral, main_borrow_amount, lp_borrow_pct)
    total_borrow = main_borrow_amount + lp_borrow_amount
    updated_curr_in_collateral = calculate_current_main_curr_in_collateral(lp_borrow_pct, total_borrow)
    stake_borrow_amount = calculate_borrow_amount_to_required_borrow_pct(
        updated_curr_in_collateral, total_borrow, total_borrow_pct)
    return lp_borrow_amount, stake_borrow_amount


def calculate_base_borrow_amount_and_then_main_borrow_required_pct(
        main_curr_in_collateral, base_curr_in_collateral, base_borrow_amount,
        main_borrow_amount, base_borrow_pct, main_borrow_pct):
    """Bx: base_curr, Bs: main_curr,
    Borrow Bx and convert it to LP and stake on tarot, then borrow Bs amount and convert it to LP
    and then stake it on other website."""
    base_additional_borrow = calculate_borrow_amount_converted_to_lp_to_required_borrow_pct(
        base_curr_in_collateral, base_borrow_amount, base_borrow_pct)
    updated_main_curr_in_collateral = main_curr_in_collateral + int(
        (base_additional_borrow / 2) * (main_curr_in_collateral / base_curr_in_collateral))
    main_additional_borrow = calculate_borrow_amount_converted_to_lp_to_required_borrow_pct(
        updated_main_curr_in_collateral, main_borrow_amount, main_borrow_pct)
    return base_additional_borrow, main_additional_borrow
