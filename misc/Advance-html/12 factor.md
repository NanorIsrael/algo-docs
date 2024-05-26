https://12factor.net/


The 12-Factor App is a methodology for building software-as-a-service (SaaS) applications that are designed to be robust, scalable, and maintainable. This methodology was introduced by Heroku to provide guidelines for best practices in modern web application development. The 12 factors are:

Codebase: One codebase tracked in version control, many deploys. Each app should have a single codebase, which is stored in a version control system (like Git), and can be deployed to multiple environments.

Dependencies: Explicitly declare and isolate dependencies. An app should declare all its dependencies completely and use dependency isolation tools (like virtual environments or containerization) to ensure consistency across environments.

Config: Store config in the environment. Configuration that varies between deploys (such as database URLs or credentials) should be stored in environment variables, not in the code.

Backing Services: Treat backing services as attached resources. All external resources (databases, message queues, caches) should be treated as attached resources that can be attached or detached via configuration.

Build, Release, Run: Strictly separate build and run stages. The build stage converts code into an executable bundle, the release stage combines the build with the configuration, and the run stage runs the application.

Processes: Execute the app as one or more stateless processes. Applications should be executed in stateless processes where any state that needs to persist should be stored in a stateful backing service.

Port Binding: Export services via port binding. The application should be self-contained and expose its functionality by binding to a port, making it accessible over the network.

Concurrency: Scale out via the process model. Applications should be designed to scale out using the process model, running multiple instances of stateless processes to handle increased load.

Disposability: Maximize robustness with fast startup and graceful shutdown. Applications should be disposable, meaning they can be started and stopped quickly, and can handle unexpected termination gracefully.

Dev/Prod Parity: Keep development, staging, and production as similar as possible. Development, staging, and production environments should be as similar as possible to avoid issues that only manifest in production.

Logs: Treat logs as event streams. Applications should not concern themselves with routing or storage of their output stream. Instead, they should write their logs to stdout, and allow the execution environment to handle routing and storage.

Admin Processes: Run admin/management tasks as one-off processes. Any administrative or management tasks (such as database migrations) should be run as one-off processes in an identical environment as the app.