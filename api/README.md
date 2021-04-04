#Design Notes

###Endpoints for /api/
*/metrics/
  *GET: list all metics
  *POST: create a metric
*/metrics/int:pk
  *GET: list metric detail with all associated metrics
  *POST: create new entry
  *PUT: update metric details
  *DELETE: delete a metric
*/metrics/int:fk/int:pk
  *GET: get detail about an entry
  *PUT: update an entry
  *DELETE: delete an entry
