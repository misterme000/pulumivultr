import pulumi
import pulumi_vultr as vultr

# Define the Kubernetes cluster configuration
cluster = vultr.Kubernetes(
    "myK8sCluster",
    region="ewr",  # Use the appropriate region identifier for your deployment
    version="1.29",  # Specify the desired Kubernetes version
    node_pools=vultr.KubernetesNodePools(
        node_quantity=2,
        label="myNodePool",
        plan="vc2-2c-2gb",  # Each node will have 1 CPU and 2GB RAM
        tag="myClusterTag",
    ),
)

# Export the Kubeconfig of the cluster
pulumi.export("kubeconfig", cluster.kube_config)
