import pulumi
import pulumi_kubernetes as kubernetes
import pulumi_linode as linode

# Step 1: Create a Linode Kubernetes cluster.
# Note: This is only necessary if you don't already have an LKE cluster.
cluster = linode.LkeCluster("my-cluster",
    k8s_version="1.20",
    region="us-central",
    node_pools=[{
        "count": 1,
        "type": "g6-standard-2",
    }]
)

# Step 2: Configure the Kubernetes provider to connect to the Linode cluster.
k8s_provider = kubernetes.Provider("k8s-provider", kubeconfig=cluster.kubeconfig)

# Step 3: Deploy the Supabase Helm chart to the cluster.
supabase_chart = kubernetes.helm.v3.Chart("supabase",
    kubernetes.helm.v3.ChartOpts(
        chart="supabase",
        version="0.0.1",  # Specify the correct chart version you wish to deploy.
        fetch_opts=kubernetes.helm.v3.FetchOpts(
            repo="https://charts.supabase.io"  # This should be the repository where the Supabase Helm chart is located.
        ),
    ),
    opts=pulumi.ResourceOptions(provider=k8s_provider)
)

# Exports the kubeconfig and cluster details.
pulumi.export("kubeconfig", cluster.kubeconfig)
pulumi.export("clusterName", cluster.name)
pulumi.export("chartName", supabase_chart.name)
