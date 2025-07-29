## 📘 Data Dictionary

| Column Name                | Data Type     | Description                                               |
|----------------------------|---------------|-----------------------------------------------------------|
| hotel                      | object        | Hotel type: 'Resort Hotel' or 'City Hotel'                |
| is_canceled                | int           | 1 if booking was canceled, 0 otherwise                    |
| lead_time                 | int           | Days between booking and arrival                          |
| arrival_date              | datetime64    | Combined arrival date                                     |
| stays_in_weekend_nights   | int           | Nights stayed during weekend                              |
| stays_in_week_nights      | int           | Nights stayed during weekdays                             |
| adults                    | int           | Number of adults                                          |
| children                  | int           | Number of children                                        |
| babies                    | int           | Number of babies                                          |
| meal                      | object        | Meal type ('BB', 'HB', 'FB', 'SC', 'Other')               |
| country                   | object        | Country code of guest                                     |
| market_segment            | object        | Market category for booking                               |
| distribution_channel      | object        | Channel used for booking                                  |
| is_repeated_guest         | int           | 1 if guest has booked before, 0 otherwise                 |
| previous_cancellations    | int           | Number of past cancellations                              |
| previous_bookings_not_canceled | int     | Number of past bookings not canceled                      |
| reserved_room_type        | object        | Reserved room category                                    |
| assigned_room_type        | object        | Final assigned room category                              |
| booking_changes           | int           | Total booking modifications                               |
| deposit_type              | object        | Deposit type ('No Deposit', 'Non Refund', 'Refundable')   |
| agent                     | float         | ID of agent (0 if no agent)                               |
| company                   | float         | ID of company (0 if no company)                           |
| days_in_waiting_list      | int           | Days booking waited on the waiting list                   |
| customer_type             | object        | Type of customer                                          |
| adr                       | float         | Average Daily Rate (EUR)                                  |
| required_car_parking_spaces | int         | Parking spaces requested                                  |
| total_of_special_requests | int           | Number of special requests                                |
| reservation_status        | object        | Status: Canceled, No-Show, Check-Out                      |
| reservation_status_date   | datetime64    | Date of status update                                     |
| total_guests              | int/float     | Total guests = adults + children + babies                 |