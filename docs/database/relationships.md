### Relationships between DB records
Currently, there are two DB records (except Django default ones): carriers and zones.
Zones represent the real place where the order is delivered. A carrier is a person who delivers an order to the zone.

We can have multiple zones and **each zone can be served by several carriers**. For example, when there are several orders 
to the same building. So, the relationship between carrier and a zone is **one to many**.