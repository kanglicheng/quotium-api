
class RentalEstimate(object):

    def yearly_full_home(self):
        monthly = 3732
        return monthly*12

    def yearly_airbnb_total(self):
        data = [1905, 2448, 3036, 3251, 3177, 2549, 1527,
                1117, 1145, 1155, 1172, 1973]
        return sum(data)

    def yearly_renter_rent(self):
        monthly_renter = 2887
        return monthly_renter*12
