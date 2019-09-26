The SQL query create a table called _events_ that has as columns: _device_id_, _time_stamp_ and _next_time_stamp_. The last one provides,
for each _device_id_, the _time_stamp_ of the following event. All the data is from _events_table_ and corresponds to events ocurred in _month_=201908
with _app_id_=1 and _event_id_=4.

Then, from the table _events_, creates a table called _per_event_ with columns _device_id_ and _time_diff_, wich provides the amount of time (in seconds) from one event
to the following.

Finally, selects from _per_event_ the _device_id_ and the average of _time_diff_ for each _device_id_. It presents the results ordered by _device_id_

In summary the query shows, for each user, the average time that passes from one event to the following (both with _event_id_=4) from august of 2019 and client with 
_app_id_ = 1

This query has important information that can be used in many ways. For example, it can be used to classify the users of an app based on the average time from events. Or if
we apply this query to different apps it can be used to compare and describe the frequency of use of each app.
Also, it can be used to identify anomalies in users behavior, for example if a user spend much more time than the average between events in various ocations,
we could asume that is using the app with less frequency, and probably changing the way of using it.

I don't have lot of experience with SQL but I have experience with pandas, and I'm a fast learner :)
