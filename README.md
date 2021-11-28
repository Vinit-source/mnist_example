# ML Ops Repo

# Assignment 10:

1. Serve SVM and Decision tree models using the flask on separate relative URLs. i.e. `localhost:8000/svm_predict` and `localhost:8000/decision_tree_predict`. (ip could be different than localhost, in your case)
2. Dockerize the deployment i.e. create dockerfile and build image such that when you do `docker run` (may be with some more flags), the above two links should be accessible via curl. Write `docker_example.sh` shell script that includes the full curl commands.

Results:

Client side:
```bash
(mlops) vinitgore@dell-Inspiron-15-3567:/media/vinitgore/Workplace/MTech/MTechYear2Sem1/MLOps/mnist_example$ sudo docker exec 25f0d2e03e02 curl http://localhost:5000/svm_predict -X POST  -H 'Content-Type: application/json' -d '{"image":["0.0","0.0","0.0","2.000000000000008","12.99999999999999","2.3092638912203262e-14","0.0","0.0","0.0","0.0","0.0","7.99999999999998","14.999999999999988","2.664535259100375e-14","0.0","0.0","0.0","0.0","4.9999999999999885","15.999999999999975","5.000000000000027","2.0000000000000027","3.552713678800496e-15","0.0","0.0","0.0","14.999999999999975","12.000000000000007","1.0000000000000182","15.999999999999961","4.000000000000018","7.1054273576009955e-15","3.5527136788004978e-15","3.9999999999999925","15.999999999999984","2.0000000000000275","8.999999999999984","15.999999999999988","8.00000000000001","1.4210854715201997e-14","3.1554436208840472e-30","3.5527136788004974e-15","9.999999999999995","13.999999999999986","15.99999999999999","16.0","4.000000000000025","7.105427357601008e-15","0.0","0.0","0.0","0.0","12.999999999999982","8.000000000000009","1.4210854715202004e-14","0.0","0.0","0.0","0.0","0.0","12.999999999999982","6.000000000000012","1.0658141036401503e-14","0.0"]}'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   994  100     1  100   993    100  99300 --:--:-- --:--:-- --:--:-- 994004
1

(mlops) vinitgore@dell-Inspiron-15-3567:/media/vinitgore/Workplace/MTech/MTechYear2Sem1/MLOps/mnist_example$ sudo docker exec 25f0d2e03e02 curl http://localhost:5000/svm_predict -X POST  -H 'Content-Type: application/json' -d '{"image":["0.0","0.0","0.0","2.000000000000008","12.99999999999999","2.3092638912203262e-14","0.0","0.0","0.0","0.0","0.0","7.99999999999998","14.999999999999988","2.664535259100375e-14","0.0","0.0","0.0","0.0","4.9999999999999885","15.999999999999975","5.000000000000027","2.0000000000000027","3.552713678800496e-15","0.0","0.0","0.0","14.999999999999975","12.000000000000007","1.0000000000000182","15.999999999999961","4.000000000000018","7.1054273576009955e-15","3.5527136788004978e-15","3.9999999999999925","15.999999999999984","2.0000000000000275","8.999999999999984","15.999999999999988","8.00000000000001","1.4210854715201997e-14","3.1554436208840472e-30","3.5527136788004974e-15","9.999999999999995","13.999999999999986","15.99999999999999","16.0","4.000000000000025","7.105427357601008e-15","0.0","0.0","0.0","0.0","12.999999999999982","8.000000000000009","1.4210854715202004e-14","0.0","0.0","0.0","0.0","0.0","12.999999999999982","6.000000000000012","1.0658141036401503e-14","0.0"]}'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   994  100     1  100   993    100  99300 --:--:-- --:--:-- --:--:-- 99400
4

(mlops) vinitgore@dell-Inspiron-15-3567:/media/vinitgore/Workplace/MTech/MTechYear2Sem1/MLOps/mnist_example$ sudo docker exec 25f0d2e03e02 curl http://localhost:5000/tree_predict -X POST  -H 'Content-Type: application/json' -d '{"image": ["0.0","0.0","0.0","11.999999999999982","13.000000000000004","5.000000000000021","8.881784197001265e-15","0.0","0.0","0.0","0.0","10.999999999999986","15.999999999999988","9.000000000000005","1.598721155460224e-14","0.0","0.0","0.0","2.9999999999999925","14.999999999999979","15.999999999999998","6.000000000000022","1.0658141036401509e-14","0.0","6.217248937900871e-15","6.999999999999987","14.99999999999998","15.999999999999996","16.0","2.0000000000000284","3.552713678800507e-15","0.0","5.5220263365470826e-30","6.21724893790087e-15","1.0000000000000113","15.99999999999998","16.0","3.000000000000022","5.32907051820075e-15","0.0","0.0","0.0","0.9999999999999989","15.99999999999998","16.0","6.000000000000015","1.0658141036401498e-14","0.0","0.0","0.0","0.9999999999999989","15.99999999999998","16.0","6.000000000000018","1.0658141036401503e-14","0.0","0.0","0.0","0.0","10.999999999999986","15.999999999999993","10.00000000000001","1.7763568394002505e-14","0.0"]}'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   991  100    12  100   979   1333   106k --:--:-- --:--:-- --:--:--  107k
Prediction1

(mlops) vinitgore@dell-Inspiron-15-3567:/media/vinitgore/Workplace/MTech/MTechYear2Sem1/MLOps/mnist_example$ sudo docker exec 25f0d2e03e02 curl http://localhost:5000/tree_predict -X POST  -H 'Content-Type: application/json' -d '{"image":["0.0","0.0","0.0","2.000000000000008","12.99999999999999","2.3092638912203262e-14","0.0","0.0","0.0","0.0","0.0","7.99999999999998","14.999999999999988","2.664535259100375e-14","0.0","0.0","0.0","0.0","4.9999999999999885","15.999999999999975","5.000000000000027","2.0000000000000027","3.552713678800496e-15","0.0","0.0","0.0","14.999999999999975","12.000000000000007","1.0000000000000182","15.999999999999961","4.000000000000018","7.1054273576009955e-15","3.5527136788004978e-15","3.9999999999999925","15.999999999999984","2.0000000000000275","8.999999999999984","15.999999999999988","8.00000000000001","1.4210854715201997e-14","3.1554436208840472e-30","3.5527136788004974e-15","9.999999999999995","13.999999999999986","15.99999999999999","16.0","4.000000000000025","7.105427357601008e-15","0.0","0.0","0.0","0.0","12.999999999999982","8.000000000000009","1.4210854715202004e-14","0.0","0.0","0.0","0.0","0.0","12.999999999999982","6.000000000000012","1.0658141036401503e-14","0.0"]}'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1005  100    12  100   993   1333   107k --:--:-- --:--:-- --:--:--  109k
Prediction4
```

Server side: 
```bash
(mlops) vinitgore@dell-Inspiron-15-3567:/media/vinitgore/Workplace/MTech/MTechYear2Sem1/MLOps/mnist_example$ sudo docker run -it -p 5000:5000 mnist:latest 
 * Serving Flask app 'app' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 229-714-809
Model loaded.
127.0.0.1 - - [28/Nov/2021 17:56:26] "POST /svm_predict HTTP/1.1" 200 -
Model loaded.
127.0.0.1 - - [28/Nov/2021 17:57:55] "POST /svm_predict HTTP/1.1" 200 -
Model loaded.
127.0.0.1 - - [28/Nov/2021 17:58:07] "POST /tree_predict HTTP/1.1" 200 -
Model loaded.
127.0.0.1 - - [28/Nov/2021 17:58:30] "POST /tree_predict HTTP/1.1" 200 
```
