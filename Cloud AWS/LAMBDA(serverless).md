## SERVERLESS
---

1. You don't own server.

2. Zero mainatainance.

3. Salablity automatic.


    Suppose you have EC2-Server which takes 4GB memory, 500GB Hard Disk,2 core processor which are charged on running mode.
Even if 100% utilization is not done then also you have to pay full charges of 1005 usage.
     

**LAMBDA FUNCTION**
---
   
   1.No Server.
   
   2.Code storage - No cost

   3.When code in running mode - Cost

    Cost is calculated on usage of `(CPU + RAM) * TIME = CHARGE`.
- AWS Lambda lets you run code without provisioning or managing servers. You pay only for the compute time you consume.
 
No charges of OS. 
It also contains *scalability* and *parallelization*.
  
**Scalablity**
   
    Scale up and Scale down is automatic.
    
eg: 1. 1GB memory, 2 Core - 30 sec

    2. updated -> 2GB , 1 Core - 10 sec

**Parallelization** 

    On every execution request, if simultaneous 1 million requests occurs Lambda will handel every 
    request simultaneously.
    
[Referance](https://aws.amazon.com/lambda/)
