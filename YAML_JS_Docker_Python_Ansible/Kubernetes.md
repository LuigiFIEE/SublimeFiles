## Kubernetes introduction ##

Its a containers orchestation


-- Components:

 * Master Server:

 	API Server 
 	Controller Manager (create PODs)
 	Schudeler

 Database is ETCD for Master Server

 *	Worker:

 Server que tiene kubelet 
 Dentro hay un POD

 *	Services:
 	Load Balancer





-- See all PODs with process

	kubctl get all 

	NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
	service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   4d13h
