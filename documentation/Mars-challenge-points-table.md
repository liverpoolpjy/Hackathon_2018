
# Points Distribution Table

For each one of the tasks completed your team will get points. These Points will
be added at the end of the Challenge. The team that has the most points will win
 the challenge
 
#### Notes:
    Below the terms like "in container" or "run in Docker container" mean packaging the service into a dedicated Docker image and luanch the service outside container. An example to lauch a in-container service is "docker run imageName /usr/bin/myService". SSH into container or using a interactive shell is not allowed.


## Challenge Competition

|####|Name|Description|Points|
|----|----|-----------|------|
|CC-1|Level Up!|Connect to Game Center to participate competition| 5|
|CC-2|Challenge Champion|AI Battle Competition score for each turn. | No.1 : 49<br> No.2 : 38<br> No.3 : 32<br> No.4 : 26<br> No.5 : 20|

If there is a tie within one turn for a pair of team, their ranks are equally marked the lower rank value, e.g.: Rank-1, Rank-3 (tied team), Rank-3 (tied team), Rank-4, Rank-5.
CC-2 AI Battle includes 3 turns, the final CC-2 score for one team is calculated by: sum{No.X score of each turn} / 3

## Sensor Suite

|####|Name|Description|Points|
|----|----|-----------|------|
|S-1 |Basic|Successfully deploy and run all sensor suite service, including flare, publisher, radiation and temperature, with at least one service deployed in Cloud Machine. |5|
|S-2 |Deploy in Raspberry Pi| At least one sensor suit service is deployed Raspberry Pi|5|
|S-3 |Deploy in Docker|All sensor suite services are deployed in Docker container|5|
|S-4 |Docker in Raspberry Pi|At least on above Docker container is deployed in Raspberry Pi|5|

## Aggregator

|####|Name|Description|Points|
|----|----|-----------|------|
|A-1|Basic| Successfully deploy and run aggregator|2.5|


## Team Solution

|####|Name|Description|Points|
|----|----|-----------|------|
|T-1 |Solution in container|Deploy the team AI battle solution in Docker container|5|


## Game Controller

|####|Name|Description|Points|
|----|----|-----------|------|
|G-1|Basic|Successfully deploy and run game controller in competitor’s environment|2.5|


## Integration

|####|Name|Description|Points|
|----|----|-----------|------|
|I-1|Basic| Successfully connect services of S-1, A-1, T-1 and G-1 and run through the game challenge|5|
|I-2|Dynamically connection| The above components are all deployed in different containers and can be connected by non-static IP method, such as communication by resolving their hostname with the help of DNS|5|
|I-3|Deploy by PaaS|The above components are all deployed in different containers by using Kubernetes or Docker Swarm or Mesos|5|
|I-4|Replias|Able to tell which service in sensor suites can be scaled and can control the replias of it/them.|5|

If there is a WHOLE-score tie between a pair of team, they use more added CC-2 turns to distinguish for their unique rank, not influencing ranks of other teams.
The rank of tied teams will be distinguished by their earlist CC-2 turn that makes a distinguishiable score value: No.X score of this added turn


