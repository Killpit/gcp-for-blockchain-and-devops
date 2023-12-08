# Google Cloud IAM

Google Cloud IAM allows you to manage resources with principle of least privilege, which states that nobody should have more permissions they need.

## Components

## How IAM Works

- IAM allows organizations to manage who can do what with given resources. In Google Cloud, resources are also defined as organizations, folders and projects that are used to organize other resources unlike in other cloud providers.

- Permissions are grouped into roles and roles are granted to authenticated principals/members instead of granting permissions directly to users.

- IAM policy defines what resources can be accessed and used by the users. When authenticated members access resources, IAM first checks the resource's allow policy to determine whether the action is permitted, then allows access to resources if permitted. Also, deny policies can be used to prevent specific users from using IAM permissions.

### Model Access Management

#### Principal

- Google Accounts for end users
- Service accounts for application and compute workloads
- Google Group
- Google Workspace account
- Cloud Identity domain that can access a resource
- Have their own identifiers

#### Role

- Collection of permissions.
- Determine what operations are allowed on a resource.
- When granted to a principal, permissions that the role contains are granted to the role that contains.

#### Policy

Policies are bindings that binds roles to one or more principals to individual roles. When you define employees' access to roles on a resource, an allow policy is created and attached it to the resource.