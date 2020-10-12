    
3. Write at least 10 `manual test cases` for the most common use cases. Write them with this template:

```text
Test-id: CLI-1
Test-name: CLI option "service"
Description: When argument service=<component> is provided the deployment tool should deploy given packet.
Pre-requisites: The packet provided exist
Test-steps:
    1. Start deploy_cli.py
    2. Use the command `deploy service=frontend`
Expected-result:
    The CLI tool print correct logs
    The correct package is deployed
```
============================================================================================================

```text
Test-id: CLI-1
Test-name: CLI option 'region' 'eu-west-1'
Description: When argument region=eu-west-1 is provided the deployment tool should deploy to that region.
Pre-requisites:
Test-steps:
    1. Start deploy_cli.py
    2. Use the command `deploy region=eu-west-1`
Expected-result:
    The CLI tool print correct logs
    The correct package is deployed
```

```text
Test-id: CLI-2
Test-name: CLI option 'region' 'us-south-1'
Description: When argument region=us-south-1 is provided the deployment tool should deploy to that region.
Pre-requisites:
Test-steps:
    1. Start deploy_cli.py
    2. Use the command `deploy region=us-south-1`
Expected-result:
    The CLI tool print correct logs
    The correct package is deployed
```

```text
Test-id: CLI-3
Test-name: CLI option 'region' invalid
Description: When argument region=blub is provided the deployment tool should fail to deploy and exit with code 255
Pre-requisites:
Test-steps:
    1. Start deploy_cli.py
    2. Use the command `deploy region=blub`
Expected-result:
    The CLI tool fails to deploy
    The CLI tool exits with code 255
```

```text
Test-id: CLI-4
Test-name: CLI option 'conf' 'production'
Description: When argument conf=production is provided the deployment tool should deploy to production
Pre-requisites:
Test-steps:
    1. Start deploy_cli.py
    2. Use the command `deploy conf=production`
Expected-result:
    The CLI tool print correct logs
    The correct package is deployed
```

```text
Test-id: CLI-5
Test-name: CLI option 'service' 'frontend'
Description: When argument service=frontend is provided the deployment tool should deploy that service.
Pre-requisites:
Test-steps:
    1. Start deploy_cli.py
    2. Use the command `deploy service=frontend`
Expected-result:
    The CLI tool print correct logs
    The CLI tool deploys the frontend service
```

```text
Test-id: CLI-6
Test-name: CLI option 'timeout' 'minutes'
Description: When argument timeout=5m is provided the deployment tool should cancel the deployment if it takes longer than 5min
Pre-requisites: The deployment job takes more than 5minutes
Test-steps:
    1. Start deploy_cli.py
    2. Use the command `deploy timeout=1m`
Expected-result:
    The CLI tool print correct logs
    The deployment tool timeouts after 5m and exits with code 255
```

```text
Test-id: CLI-7
Test-name: CLI option 'cluster' (DNS) 'example.com'
Description: When argument cluster=example.com is provided the deployment tool should deploy to that cluster.
Pre-requisites:
Test-steps:
    1. Start deploy_cli.py
    2. Use the command `deploy cluster=example.com`
Expected-result:
    The CLI tool print correct logs
    The deployment tool deploys to the provided cluster
```

```text
Test-id: CLI-8
Test-name: CLI option 'cluster' (IP) '127.0.0.1'
Description: When argument cluster=127.0.0.1 is provided the deployment tool should deploy to that cluster
Pre-requisites: The cluster exists
Test-steps:
    1. Start deploy_cli.py
    2. Use the command `deploy cluster=127.0.0.1`
Expected-result:
    The CLI tool print correct logs
    The CLI tool deploys to the provided cluster
```

```text
Test-id: CLI-9
Test-name: CLI option 'conf' 'test'
Description: When argument conf=test is provided the deployment tool should deploy to test
Pre-requisites:
Test-steps:
    1. Start deploy_cli.py
    2. Use the command `deploy conf=test`
Expected-result:
    The CLI tool print correct logs
    The correct package configuration is deployed
```

```text
Test-id: CLI-10
Test-name: CLI option 'service' 'backend'
Description: When argument service=backend is provided the deployment tool should deploy that service.
Pre-requisites:
Test-steps:
    1. Start deploy_cli.py
    2. Use the command `deploy service=backend`
Expected-result:
    The CLI tool print correct logs
    The CLI tool deploys the backend service
```

```text
Test-id: CLI-11
Test-name: CLI invalid arg format
Description: When an invalid argument format (no =) is passed the program should exit with code 255
Pre-requisites:
Test-steps:
    1. Start deploy_cli.py
    2. Use the command `deploy conf`
Expected-result:
    The CLI tool print the correct logs
    The CLI tool exits with code 255
```


4. Manual testing is time consuming, is it possible to write `unit tests` for parts of the code? Is there any part that are hard to test? why?

Vi kan skriva unit tests för att se hurudivda programmet krashar om vi ger den felaktigt input.
Vi kan skriva unit tests för att se att den kan hantera alla argument som den ska hantera enligt specifikationen.

Detta kan vi ("enkelt") skriva unit tests för:

*   utils.parse
    *   return type: dict
    *   correct return values
*   utils.dict_to_string
    *   return type: string
    *   correctly formatted string.

*   validation.validate_args
    *   Den kan hantera de options som finns.
    *   raises ValidationError if arg is invalid

*   validation.validate_deploy_options
    *   raise TypeError if not options is a dict
    *   raise ValidationError if any options is invalid
    *   255 if conf not in options
*   validation.validate_conf
    *   raises TypeError if not string
    *   does not raise error if string

Detta är svårare att skriva unit tests för:
*   cloud_sdk.fake_deploy - vi kan inte testa för att det tar tid.
*   api.deploy - samma som ovan.
*   validation.return_on_except - hur skriver man tester för en dekorator?
*   DeployTool - hur skriver man unit tests för cmd?
*   Kan man/hur testa importer?


5. Start writing unit tests as a team, focus on the most important test cases. Then also take coverage into consideration (you can run `tox`)