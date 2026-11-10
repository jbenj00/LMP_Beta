# Script properties — searchable symbol index

Source: `schemas/scriptproperties.xml`. A property may depend on its datatype and inheritance.

## `component` (147 direct properties)

- `exists` → `true iff the component exists in the game graph`
- `isoperational` → `true iff the component exists in the game graph and is operational`
- `iswreck` → `true iff the component exists in the game graph and is wrecked`
- `isconstruction` → `true iff the component exists in the game graph and is in construction state`
- `issurfaceelement` → `true iff the component is a surface element`
- `isclass.{$class}` → `true iff the component exists and is of the given class`
- `isclass.<classname>` → `Shortcut for isclass.{class.<classname>}`
- `isclass.{$list}` → `true iff the component exists and is of one of the classes in the list`
- `isrealclass.{$class}` → `true iff the component exists and is really of the given class, regardless of current state`
- `isrealclass.<classname>` → `Shortcut for isrealclass.{class.<classname>}`
- `isrealclass.{$list}` → `true iff the component exists and is really of one of the classes in the list, regardless of current state`
- `canbeattacked` → `true iff the component exists in the game graph, is not a wreck, and is either operational, is of real class station, or is a child of a station`
- `extension` → `Source extension id`
- `isextensionpersonal` → `true iff the source extension is personal`
- `class` → `Component class`
- `realclass` → `Real component class, regardless of current state`
- `state` → `Component state`
- `macro` → `Component macro`
- `grouptag` → `Parent group tag`
- `parent` → `Parent component`
- `container` → `Container context`
- `controllable` → `Controllable context`
- `defensible` → `Defensible context`
- `object` → `Object context`
- `ship` → `Ship context`
- `station` → `Station context`
- `cluster` → `Cluster context`
- `sector` → `Sector context`
- `zone` → `Zone context`
- `room` → `Room context`
- `module` → `Module context`
- `hascontext.{$component}` → `true iff this is in the context of the other component`
- `commoncontext.{$component}` → `The common context between two components`
- `canbelivestreamed` → `true if the component is currently suitable to be featured in a live stream`
- `isinternallystored` → `true if the component is inside an internal dockingbay`
- `seed` → `Persistent pseudo-random seed (highest level of randomness supported for classes npc and dockingbay)`
- `generationseed` → `(output only)Current seed value defined by its source (e.g. god or script action) to be used for generation of an object when passed as 'seed' into random evaluators. Null if seed is not defined.`
- `name` → `Display name`
- `rawname` → `Raw display name, as text entry reference unless renamed manually`
- `knownname` → `Display name, ignoring the unknown-status`
- `hasbeenrenamed` → `true iff the component has been renamed`
- `debugname` → `Debug name comprised of knownname, idcode and id`
- `position` → `Position relative to parent`
- `relativeposition.{$component}` → `Position relative to $component`
- `relativeposition.{$componentslot}` → `Position relative to $componentslot`
- `rotation` → `Rotation relative to parent`
- `relativerotation.{$component}` → `Rotation relative to $component`
- `relativerotation.{$componentslot}` → `Rotation relative to $componentslot`
- `velocity` → `Linear velocity relative to the cluster, but relative to the component's rotation (in m/s)`
- `speed` → `Speed relative to the cluster (in m/s)`
- `relvelocity` → `Linear velocity relative to the component's parent, but relative to the component's rotation (in m/s)`
- `relspeed` → `Speed relative to the component's parent (in m/s)`
- `attention` → `Attention level`
- `size` → `Size (based on bounding box)`
- `safesize` → `Rotationally agnostic size (based on bounding box)`
- `length` → `Length (size in Z dimension, based on bounding box)`
- `height` → `Height (size in Y dimension, based on bounding box)`
- `width` → `Width (size in X dimension, based on bounding box)`
- `owner` → `Owner faction (cover owner if set, otherwise true owner)`
- `coverowner` → `Cover Owner faction`
- `trueowner` → `true Owner faction`
- `isplayerowned` → `true iff owned by player (true owner)`
- `isownerless` → `true iff ownerless (faction Ownerless)`
- `distanceto.{$component}` → `Distance to other component`
- `distanceto.{$position}` → `Distance to $position relative to parent`
- `distanceto.{$componentslot}` → `Distance to component and connection offset of $componentslot`
- `distanceto.[$component, $position]` → `Distance to $position relative to other component (space)`
- `bboxdistanceto.{$component}` → `Distance from this component's bounding box to other component's bounding box`
- `bboxdistanceto.{$position}` → `Distance from this component's bounding box to $position relative to parent`
- `bboxdistanceto.{$componentslot}` → `Distance from this component's bounding box to component and connection offset of $componentslot`
- `bboxdistanceto.[$component, $position]` → `Distance from this component's bounding box to $position relative to other component (space)`
- `bboxdistanceto.[$component, $position, $sizeobject]` → `Distance from this component's bounding box to bounding box of $sizeobject at $position relative to other component (space) ($sizeobject may be identical to $component)`
- `gatedistance.{$component}` → `Number of gates to other component. Providing cluster leads to using a random sector. The gate distance is -1 if the other component is unreachable via a path through the galaxy.`
- `gatedistance.{$component}.{$refobject}` → `Number of known gates to other component for reference object. Providing cluster leads to using a random sector`
- `gatedistance.{$component}.{$blacklistgroup}.{$refobject}` → `Number of known gates to other component using sector travel blacklist for reference object, defaulting to specified group blacklist if object doesn't have one. Providing cluster leads to using a random sector. The gate distance is -1 if the other component is unreachable via a path through the galaxy.`
- `isblacklisted.{$blacklisttype}.{$blacklistgroup}.{$refobject}` → `true if this component is included in specified blacklist for reference object, defaulting to specified group blacklist if object doesn't have one`
- `isknown` → `true iff the component is known to the player`
- `isrelationchangedisabled` → `true iff the component has been flagged to not change its relation to others`
- `hasrelation.<relationrange>.{$component}` → `true iff the relation to owner of other component is in specified range`
- `hasrelation.<relationrange>.{$faction}` → `true iff the relation to $faction is in specified range`
- `relationto.{$component}` → `Relation to owner of other component`
- `relationto.{$faction}` → `Relation to $faction`
- `relationchange.attacktolerance.threshold` → `Threshold until attacks are no longer considered friendly fire`
- `relationchange.attacktolerance.absolute` → `Absolute tolerance value to be set on attack`
- `relationchange.attacktolerance.change` → `Change to tolerance value per attack`
- `relationchange.attacktolerance.decay` → `Rate at which tolerance decays back to 0`
- `relationchange.attacktolerance.delay` → `Delay until tolerance begins to decay back to 0`
- `relationchange.attackboost.absolute` → `Absolute relation boost value to be set on hostile attack against component`
- `relationchange.attackboost.change` → `Change to relation boost value per attack against component`
- `relationchange.attackboost.decay` → `Rate at which relation boost decays back to default (faction) relation`
- `relationchange.attackboost.delay` → `Delay until relation boost begins to decay`
- `relationchange.attackfaction.scan` → `Change to faction relation per detected illegal scan of a station`
- `relationchange.attackfaction.hack` → `Change to faction relation per detected hack of a station`
- `relationchange.killboost.absolute` → `Absolute relation boost value to be set on kill of component`
- `relationchange.killboost.change` → `Change to relation boost value per kill of component`
- `relationchange.killboost.decay` → `Rate at which relation boost decays back to default (faction) relation`
- `relationchange.killboost.delay` → `Delay until relation boost begins to decay`
- `relationchange.killfaction.change` → `Change to faction relation per kill of component`
- `relationchange.killfaction.bonus` → `Change to faction relation per kill of nearby enemy object`
- `relationchange.policefaction.change` → `Change to police faction relation when player is reported for attack on object`
- `relationchange.policefaction.scan` → `Change to police faction relation when player is reported for illegal scanning of an object`
- `relationchange.policefaction.hack` → `Change to police faction relation when player is reported for hacking an object`
- `relationchange.policefaction.bounty` → `Bounty money that the player gets for killing an enemy while playing police`
- `relationchange.repairboost.absolute` → `Absolute relation boost value to be set on repair of component (NYI)`
- `relationchange.repairboost.change` → `Change to relation boost value per repair of component (NYI)`
- `relationchange.repairfaction.change` → `Change to faction relation per repair of component (NYI)`
- `mayattack.{$component}` → `true if this component has a kill relation towards other component, or has a killmilitary relation and the other component has the purpose 'fight' (can be overridden by fire authorisation override)`
- `mayattack.{$faction}` → `true if this component has a kill relation towards the faction (can be overridden by fire authorisation override)`
- `ishostileto.{$component}` → `true if mutual object relations and fire authorisations allow either side to attack (see mayattack)`
- `ishostileto.{$faction}` → `true if mutual object and faction relations and fire authorisations allow either side to attack (see mayattack)`
- `wares` → `Wares`
- `haslicence.<licencetype>.{$faction}` → `true iff the component has the specified licence`
- `signal.<signalid>.name` → `name for specified signal`
- `signal.<signalid>.rawname` → `rawname for specified signal`
- `signal.<signalid>.description` → `description for specified signal`
- `signal.<signalid>.response.id` → `default response id for specified signal`
- `signal.<signalid>.response.name` → `default response name for specified signal`
- `signal.<signalid>.response.rawname` → `default raw response name for specified signal`
- `signal.<signalid>.response.description` → `default response description for specified signal`
- `signal.<signalid>.shouldaskplayer` → `whether to ask player before responding to especified signal`
- `revealedpercentage` → `Revealed percentage (average revealed percentage of all info points if applicable)`
- `revealedlevelpercentage.{$level}` → `Revealed percentage of the provided level (average revealed percentage of all info points if applicable)`
- `isinfounlocked.<infotype>` → `true iff info is unlocked for the player`
- `scannedlevel` → `Scanned level of component (-1 if not scanned by player)`
- `maxlegalscanlevel.{$component}` → `Max legal scan level when component scans other component (takes licences into account)`
- `maxlegalscanlevel.{$faction}` → `Max legal scan level when scanning object of faction (takes licences into account)`
- `gravidarfactor` → `Current gravidar factor for this component. Only valid if component is a scanning object. May reduce to zero in certain gravidar affecting regions.`
- `secrecylevel` → `Secrecy level of component`
- `haswaypoint.{$list}` → `true iff this component has at least one waypoint matching all tags (also checks child components, stopping when it reaches an Object)`
- `haswaypointpath.{$list}` → `true iff this component has at least one waypoint matching all tags (also checks child components, stopping when it reaches a component that has its own waypoint paths)`
- `haswaypointpath.{$grouptag}.{$list}` → `true iff this component has at least one waypoint matching the group and all tags ($grouptag is allowed to be null; also checks child components, stopping when it reaches a component that has its own waypoint paths)`
- `isactive` → `Is active`
- `isphysicsready` → `true iff all collision meshes for this component are loaded and ready`
- `canbedismantled` → `true if this component can currently be dismantled`
- `phase.current.exists` → `true iff there is a valid animation phase`
- `phase.current.id` → `The ID of the currently active phase`
- `phase.current.starttime` → `The start time of the currently active phase`
- `phase.current.transitions` → `The phases that can be started right now`
- `phase.current.propagation.speed` → `The propagation speed of the currently active phase, in m/s (0 if there is none)`
- `phase.current.propagation.arrivaltime.{$component}` → `The time at which the propagation of the current phase has reached or is going to reach the specified component (-1 if there is no active propagation)`
- `phase.scheduled.exists` → `true iff an animation phase is scheduled to activate`
- `phase.scheduled.id` → `the ID of the scheduled phase`
- `phase.scheduled.starttime` → `The start time of the scheduled phase`
- `phase.scheduled.transitions` → `The phases that can be started after the scheduled phase has activated`
- `phase.scheduled.propagation.speed` → `The propagation speed of the scheduled phase, in m/s (0 if there is none)`
- `phase.scheduled.propagation.arrivaltime.{$component}` → `The time at which the propagation of the scheduled phase is going to reach the specified component (-1 if there is no active propagation)`
- `resourceprobescantime` → `The additional time it takes to evaluate all resource probes owned by the component's faction in the component's current sector`

## `destructible` — inherits `component` (26 direct properties)

- `isfunctional` → `true iff the object exists in the game graph and is functional`
- `ishackable` → `true iff the object can be hacked`
- `ishacked` → `true iff the object is currently hacked`
- `isindestructible` → `true iff object has hull, is not invulnerable, and has a minimum hull value of 0`
- `ishullunrepairable` → `true iff object has hull and hull is set to unrepairable`
- `isrepairable` → `true iff the object is operational but may be repaired`
- `isinvulnerable` → `true iff the object has permanently invulnerable hull or shields`
- `isshieldunrepairable` → `true iff object has shields and shield is set to unrepairable`
- `ismodular` → `Whether a destructible is modular`
- `hull` → `Hull value`
- `maxhull` → `Max hull value`
- `hullpercentage` → `Hull value percentage`
- `shield` → `Shield value`
- `maxshield` → `Max shield value`
- `shieldpercentage` → `Shield value percentage`
- `shieldgrouptag` → `The tag of the shield group this object belongs to`
- `drop` → `Drop ID (null if not defined)`
- `hasstorage` → `true iff there is a functional storage module`
- `canclaimownership` → `true iff this object can claim ownership of a sector`
- `modulesets` → `List of module set strings`
- `makerraces` → `Maker race list`
- `primarypurpose` → `The object's primary purpose`
- `ismilitary` → `true iff the object is deemed a military object, usually based on its class and primary purpose`
- `threatscore` → `The object's threat score, either defined by its macro or by defaults based on its primary purpose`
- `lastattacker` → `The component (not exclusive to objects) that was last registered as the attacker of this object. May become null if attacker is killed.`
- `lastattacktime` → `The gametime that an attack was last registered against this object. -1s if this object has never been attacked.`

## `object` — inherits `destructible` (98 direct properties)

- `cansee.{$component}` → `true if target component is detected by gravidar of this object`
- `isinliveview` → `true if object is visible on the player's gravidar or by any player-owned object`
- `currentradarrange` → `Current radar range, accounting for gravidarfactor`
- `maxradarrange` → `Maximal radar range`
- `formationleader` → `The leader of the objects formation`
- `currentformationwingmen` → `List of ships currently in formation led by $object`
- `idcode` → `The ID Code of the object as a string (format: AAA-123)`
- `isformationleader` → `true if is a formation leader`
- `isformationwingman` → `true if is formation wingman`
- `iscommandeerable` → `true if object is commandeerable`
- `iscommandeered` → `true if object is currently commandeered`
- `isgodobject` → `true if object is a god created object`
- `isgodobjectentry` → `true if object is a god created object from an object entry`
- `isgodshipentry` → `true if object is a god created object from a ship entry`
- `isgodstationentry` → `true if object is a god created object from a station entry`
- `isgodproductionentry` → `true if object is a god created object from a production entry`
- `isgamestartgodentry` → `true if object is a god object created at gamestart`
- `isrespawnablegodobject` → `true if object is a god object flagged to be respawnable`
- `godentry` → `god entry ID (isgodobjectentry, isgodshipentry, isgodstationentry and isgodproductionentry properties can be used to determine whether this is a god object entry, god station entry or god production entry respectively)`
- `godentryname` → `god entry name`
- `godentrytags` → `list of category tags defined for the god entry`
- `hasgodentrytag.{$tag}` → `true if the god entry specifies this category tag`
- `ismasstraffic` → `true if this is a mass-traffic object`
- `ishighwaytraffic` → `true if this is a highway-traffic object`
- `istemptraffic` → `true if this is a temp-traffic object (e.g. mass or highway traffic)`
- `iszonechangepending` → `true if the remaining waypoints will result in at least one more zone-change`
- `numwaypoints` → `Number of remaining waypoints in path`
- `region` → `Associated region`
- `ismission` → `true iff object was spawned using a mission cue`
- `missioncue` → `mission cue used to spawn object`
- `isradarvisible` → `true iff visible to radar and UI`
- `canbepickedup` → `true iff object can be picked up`
- `canbepickedupby.{$ship}` → `true iff object can be picked up by the specified $ship`
- `canbetowed` → `true iff object can be towed`
- `tugship` → `the ship towing this object`
- `boost.available` → `true iff the object has a booster which can be activated right now`
- `boost.active` → `true iff the object is currently boosting`
- `boost.maxspeed` → `Maximum boost speed with present engine set up and conditions (in m/s)`
- `boost.maxduration` → `Maximum boost duration with present engine set up and conditions (in s)`
- `boost.remainingduration` → `Currently remaining boost duration until energy is depleted (in s)`
- `boost.remainingfraction` → `Currently remaining fraction of boost energy (value from 0 to 1)`
- `travel.available` → `true iff the object's travel mode can be activated right now`
- `travel.active` → `true iff the object is currently traveling`
- `travel.chargetime` → `The time in seconds until travel mode actually starts`
- `travel.charging` → `true iff the object is currently charging travel mode`
- `travel.maxspeed` → `Maximum travel speed with present engine set up and conditions (in m/s)`
- `travel.iscoasting` → `true iff the ship is currently coasting after turning off travel mode`
- `travel.disabled` → `true iff the object's travel drive is currently disabled`
- `throttle` → `the relative forward speed set for the object, value is between -1 and 1`
- `value` → `The current value of this object, including value of units and upgrades`
- `buildresourcevalue` → `The current value of this object, based on the resources required to construct itself and its units and upgrades (default build method)`
- `repairprice` → `The current repair cost of object, using average prices`
- `adsigns.numslots` → `Number of ad sign slots of this object`
- `adsigns.<state>.count` → `Number of ad signs of this object, filtered by component state: all, construction, operational or wreck`
- `adsigns.<state>.list` → `List of ad signs of this object, filtered by component state: all, construction, operational or wreck`
- `adsigns.<state>.indexof.{$component}` → `Index of $component in the list of ad signs of this object, filtered by component state (1-based), or 0 if not present`
- `adsigns.<state>.random` → `Random ad sign of this object, filtered by component state: all, construction, operational or wreck`
- `engines.numslots` → `Number of engine slots of this object`
- `engines.<state>.count` → `Number of engines of this object, filtered by component state: all, construction, operational or wreck`
- `engines.<state>.list` → `List of engines of this object, filtered by component state: all, construction, operational or wreck`
- `engines.<state>.indexof.{$component}` → `Index of $component in the list of engines of this object, filtered by component state (1-based), or 0 if not present`
- `engines.<state>.random` → `Random engine of this object, filtered by component state: all, construction, operational or wreck`
- `numsignalleakslots` → `Number of signal leak slots on the object`
- `scuttleeffect` → `The name of the effect used to represent the object being scuttled (default: blank)`
- `isonlineobject` → `true if this is an object that originates in a different universe or has been sent on an online mission`
- `isvisitor` → `true if this object is owned by a visiting faction`
- `isvisitormissionobject` → `true if this object is owned by a visiting faction and is related to an existing mission offer or accepted mission`
- `venture` → `Venture script name of the venture that object is currently embarked on`
- `venturename` → `Display name of the venture mission that the object is currently embarked on`
- `masstrafficstartobject` → `The start waypoint's object context if this is a mass traffic object`
- `masstrafficendobject` → `The end waypoint's object context if this is a mass traffic object`
- `hasenginemod` → `Whether the object has any engine mod installed`
- `hasenginemod.{$ware}` → `Whether the object has a engine mod based on the specified engine mod ware installed`
- `haspaintmod` → `Whether the object has any paint mod installed`
- `haspaintmod.{$ware}` → `Whether the object has a paint mod based on the specified paint mod ware installed`
- `equipmentmodwares` → `All equipment mod wares installed on this object`
- `isunit` → `true iff the object is a unit`
- `isdeployable` → `true iff the object is a deployable`
- `unitcategory` → `Unit category this object belongs to (null if none)`
- `deployablecategory` → `Deployable category this object belongs to (null if none)`
- `formationshape` → `The current formation shape of the object`
- `formationradius` → `The current formation radius of the object`
- `isformationrolling` → `Whether current formation rolls (see create_formation)`
- `isformationrollmembers` → `Whether current formation members roll (see create_formation)`
- `formationmaxshipsperline` → `The current formation shape of the object`
- `isinhazardousregion` → `Whether the object's current position is inside a hazardous region`
- `isatnavigableposition` → `Whether the object is currently at a navigable sector position`
- `accesslicence` → `Licence type required for access to this object (null if no restriction)`
- `accessrestricted` → `Access to this object restricted (for player assets)`
- `canberecycled` → `true iff object can be recycled`
- `recyclingwares.remaining` → `Remaining wares that would result from recycling this object`
- `recyclingwares.max` → `The potential maximum wares that would result from recycling this object`
- `canbedismantledby.{$defensible}` → `true if this component can be or currently is being dismantled by the specified defensible`
- `dismantlingobject` → `The object assigned to dismantle this object`
- `salvageclaimants` → `List of objects which have made a dismantle or tow claim on this object`
- `isdatavault` → `true iff the object is a Data Vault`
- `islandmark` → `true iff the object is a landmark`
- `isgravidarplayeraccessible` → `whether the player has access to this object's gravidar`

## `mine` — inherits `object` (6 direct properties)

- `isfriendfoe` → `Whether the mine has a friend/foe feature`
- `friendlist` → `Friend list for mine (only for mines friend/foe feature)`
- `foelist` → `Foe list for mine (only for mines friend/foe feature)`
- `target` → `Mine target`
- `isarmed` → `Whether the mine has armed itself`
- `safetydistance` → `The distance to its launcher at which the mine arms itself. Only valid if the mine is not yet armed!`

## `controllable` — inherits `object` (122 direct properties)

- `pilot` → `Pilot entity`
- `assignedpilot` → `Assigned pilot entity which may not currently be piloting`
- `aipilot` → `AI pilot entity`
- `assignedaipilot` → `Assigned ai pilot entity which may not currently be piloting`
- `defencenpc` → `Defence control entity`
- `tradenpc` → `Trade control entity`
- `tradecomputer` → `The trade computer assigned to this controllable for processing trade operations on the player-controlled ship`
- `engineer` → `Engineer`
- `shiptrader` → `Shiptrader`
- `shadyguy` → `Shady guy`
- `controlentity.default` → `Main control entity`
- `controlentity.{$controlpost}` → `Control entity of specified control post`
- `assignedcontrolentity.default` → `Assigned main control entity which may not currently be controlling`
- `assignedcontrolentity.{$controlpost}` → `Assigned control entity of specified control post which may not currently be controlling`
- `roleentity.{$seed}` → `Instanced entity representing the person of the specified seed for this object`
- `roleentity.{$npctemplate}` → `Instanced entity representing the specified person entry for this object`
- `roleentities` → `List of all instanced entity representing the people entries for this object`
- `slotactor.{$componentslot}` → `Actor reserved for the specified NPC slot or related chair slots`
- `waypointactors.{$componentslot}` → `List of entities currently moving towards the specified NPC waypoint`
- `isnpcassignmentrestricted` → `Is this object currently allowed to have NPCs assigned`
- `canhavecontrolentity.{$controlpost}` → `Can this object have a control entity of specified control post`
- `controlpostslot.{$controlpost}` → `Slot for the entity to enhabit when controlling this object`
- `order` → `Current order (which is the current order in the queue if it's enabled, otherwise the default order if it's enabled, otherwise null)`
- `nextorder` → `Next order in queue if the current order is in the queue and if the next order exists and is enabled, otherwise null (NOTE: In case of a user-created loop, the next order can be the current order)`
- `defaultorder` → `Default order if present, otherwise null`
- `orders` → `List of all orders in order queue (NOTE: in case of user-created order loops, the list begins with the current loop order, not necessarily the first loop order as shown in the UI)`
- `buildorders` → `List of all build orders in order queue (orders that are associated with an equip or repair task)`
- `tradeorders` → `List of all trade orders in order queue (orders that are associated with a trade)`
- `hasorderloop` → `Whether this ship's orders are in a loop`
- `hasblacklist.{$blacklisttype}.{$blacklistgroup}` → `true if this controllable has a blacklist of the specified type and group`
- `commander` → `Commander object (if this is a subordinate)`
- `toplevelcommander` → `Top-level commander object. May be a station or the ship that the player is flying.`
- `assignment` → `Assignment of this subordinate under the commanding object`
- `canuseassignment.{$assignment}.{$controllable}` → `Can this object use the specified assignment when subordinate to the specified commander. $assignment can be null.`
- `commanderentity` → `Commander entity (if this is a subordinate)`
- `activesubordinategroupids` → `List of subordinate group IDs with assigned ships`
- `subordinates` → `List of subordinates`
- `subordinates.{$assignment}` → `List of subordinates of the commander with the specified assignment`
- `subordinategroupassignment.{$subordinategroupid}` → `Assignment of subordinate group with specified ID`
- `subordinategroupdockoverride` → `Whether subordinate group of controllable is set to always dock at commander`
- `subordinategroupid` → `Subordinate group ID that controllable currently belongs to`
- `subordinategroupprotectedsector` → `Sector detached subordinate group is assigned to protect. Only works with assignment.positiondefence.`
- `subordinategroupprotectedposition` → `Sector position detached subordinate group is assigned to protect. Only works with assignment.positiondefence.`
- `subordinategroupreinforcefleet` → `Whether detached subordinate group of controllable should reinforce positions defended by other detached subordinate groups in its fleet when engaged in combat. Only works with assignment.positiondefence.`
- `subordinategrouprespondtodistresscalls` → `Whether detached subordinate group of controllable should respond to distress calls of their own stations in their current sector. Only works with assignment.positiondefence.`
- `subordinategroupresupplyatfleet` → `Whether detached subordinate group of controllable should repair and resupply at their fleet. Only works with assignment.positiondefence.`
- `subordinategroupattackonsight` → `Whether detached subordinate group of controllable should attack hostile targets on sight rather than only when attacked. Only works with assignment.positiondefence.`
- `subordinatesingroup.{$subordinategroupid}` → `List of direct subordinates of the commander in the specified subordinate group`
- `allsubordinates` → `List of all subordinates, including those not directly commanded by this`
- `allcommanders` → `List of all commanders, including those not directly commanding this. Sorted by hierarchical proximity to $controllable.`
- `canhavecommander.{$component}` → `true iff the $component (or its controllable context) can be a commander for this`
- `fleet.name` → `Name of fleet (empty string if not a fleet commander)`
- `fleet.iscommander` → `true if object is commander of its own fleet`
- `fleet.commander` → `Fleet commander object (top level fleet, null if that commander is not a fleet commader, e.g. is a unit or not player owned)`
- `fleetunit` → `Fleet unit of the object if it is a rebuild replacement for a fleet`
- `fleetunits` → `List of fleet units for the fleet of this object`
- `controlposts.all` → `All control posts for this object`
- `controlposts.free` → `All free control posts for this object`
- `controlposts.{$entity}` → `All control posts which the provided entity can take on for this object`
- `controlroom` → `The control room of the controllable or null`
- `haswalkableroom` → `Does controllable contain any walkable rooms, i.e. accessible to the player and NPCs? This can be false e.g. for stations with only docking bays in space or in internal storage`
- `canhavedynamicinterior` → `true if this object can contain a dynamic interior. This requires a window connection, even for interiors without windows.`
- `hasscanner` → `Does controllable have scanner software`
- `longrange` → `Does controllable have scanner software capable of a long-range scan`
- `maxscanlevel` → `The maximum scan level of this controllable's scanner`
- `software.compatible` → `Software that is compatible`
- `software.default` → `Software that is installed by default`
- `software.installed` → `Software that is currently installed (including default software)`
- `software.dock` → `The dock assist software that is currently installed`
- `software.longrange` → `The long range scanner that is currently installed`
- `software.police` → `The police scanner software that is currently installed`
- `people.{$npctemplate}` → `NPC template entry of a person on board the object (raw npctemplates can not provide information without the object as context - see npctemplateentry)`
- `people.count` → `Number of people on board the object as NPC templates (not actual NPCs)`
- `people.free` → `Amount of free space on board the object for additional people as NPC templates`
- `people.capacity` → `Maximum amount of potential space on board the object for people as NPC templates`
- `people.list` → `List of people on board the object as NPC templates (raw templates can't provide information without the object as context e.g. see $controllable.people.{$npctemplate})`
- `people.{$entityrole}.list` → `List of people on board or embarked for the object, by entityrole, as NPC templates`
- `people.{$entityrole}.count` → `Number of people on board or embarked for the object, by entityrole`
- `people.{$entityrole}.combinedskill` → `Combined skill value (between 0 and 100 per individual) of all people of this role, based on weighted skills that are relevant for the role`
- `people.{$entityrole}.potentialskill.{$entityrole}` → `Potential combined skill value (between 0 and 100 per individual) of all people of this role, based on weighted skills that are relevant for the specified other role`
- `people.{$entityrole}.{$level}.list` → `List of people on board or embarked for the object, by entityrole and the tier of skill value $level, as NPC templates`
- `people.{$entityrole}.{$level}.count` → `Number of people on board or embarked for the object, by entityrole and the tier of skill value $level`
- `people.{$entityrole}.{$level}.combinedskill` → `Combined skill value (between 0 and 100 per individual) of all people of this role and the tier of skill value $level, based on weighted skills that are relevant for the role`
- `people.{$entityrole}.{$level}.potentialskill.{$entityrole}` → `Potential combined skill value (between 0 and 100 per individual) of all people of this role and the tier of skill value $level, based on weighted skills that are relevant for the specified other role`
- `people.<entityrole>.list` → `List of people of specified role on board or embarked for the object as NPC templates`
- `people.<entityrole>.count` → `Number of people of specified role on board or embarked for the object`
- `people.<entityrole>.combinedskill` → `Combined skill value (between 0 and 100 per individual) of all people of specified role, based on weighted skills that are relevant for their role`
- `people.<entityrole>.potentialskill.{$entityrole}` → `Potential combined skill value (between 0 and 100 per individual) of all people of specified role, based on weighted skills that are relevant for the specified other role`
- `people.<entityrole>.{$level}.list` → `List of people of specified role of the tier of skill value $level on board or embarked for the object as NPC templates`
- `people.<entityrole>.{$level}.count` → `Number of people of specified role of the tier of skill value $level on board or embarked for the object`
- `people.<entityrole>.{$level}.combinedskill` → `Combined skill value (between 0 and 100 per individual) of all people of specified role of the tier of skill value $level, based on weighted skills that are relevant for the role`
- `people.<entityrole>.{$level}.potentialskill.{$entityrole}` → `Potential combined skill value (between 0 and 100 per individual) of all people of specified role of the tier of skill value $level, based on weighted skills that are relevant for the specified role`
- `availablepeople.{$npctemplate}` → `NPC template entry of a person currently on board the object (raw npctemplates can not provide information without the object as context - see npctemplateentry)`
- `availablepeople.count` → `Number of people currently on board the object as NPC templates (not actual NPCs)`
- `availablepeople.list` → `List of people currently on board the object as NPC templates (raw templates can't provide information without the object as context e.g. see $controllable.people.{$npctemplate})`
- `availablepeople.{$entityrole}.list` → `List of all people currently on board the object, by entityrole, as NPC templates`
- `availablepeople.{$entityrole}.count` → `Number of people currently on board the object, by entityrole`
- `availablepeople.{$entityrole}.combinedskill` → `Combined skill value (between 0 and 100 per individual) of all available people of this role, based on weighted skills that are relevant for the role`
- `availablepeople.{$entityrole}.potentialskill.{$entityrole}` → `Potential combined skill value (between 0 and 100 per individual) of all available people of this role, based on weighted skills that are relevant for the specified other role`
- `availablepeople.{$entityrole}.{$level}.list` → `List of people currently on board the object, by entityrole and the tier of skill value $level, as NPC templates`
- `availablepeople.{$entityrole}.{$level}.count` → `Number of people currently on board the object, by entityrole and the tier of skill value $level`
- `availablepeople.{$entityrole}.{$level}.combinedskill` → `Combined skill value (between 0 and 100 per individual) of all available people of this role and the tier of skill value $level, based on weighted skills that are relevant for the role`
- `availablepeople.{$entityrole}.{$level}.potentialskill.{$entityrole}` → `Potential combined skill value (between 0 and 100 per individual) of all available people of this role and the tier of skill value $level, based on weighted skills that are relevant for the specified other role`
- `availablepeople.<entityrole>.list` → `List of people of specified role currently on board the object as NPC templates`
- `availablepeople.<entityrole>.count` → `Number of people of specified role currently on board the object`
- `availablepeople.<entityrole>.combinedskill` → `Combined skill value (between 0 and 100 per individual) of all available people of specified role, based on weighted skills that are relevant for their role`
- `availablepeople.<entityrole>.potentialskill.{$entityrole}` → `Potential combined skill value (between 0 and 100 per individual) of all available people of specified role, based on weighted skills that are relevant for the specified other role`
- `availablepeople.<entityrole>.{$level}.list` → `List of people of specified role of the tier of skill value $level currently on board the object as NPC templates`
- `availablepeople.<entityrole>.{$level}.count` → `Number of people of specified role of the tier of skill value $level currently on board the object`
- `availablepeople.<entityrole>.{$level}.combinedskill` → `Combined skill value (between 0 and 100 per individual) of all available people of specified role of the tier of skill value $level, based on weighted skills that are relevant for the role`
- `availablepeople.<entityrole>.{$level}.potentialskill.{$entityrole}` → `Potential combined skill value (between 0 and 100 per individual) of all available people of specified role of the tier of skill value $level, based on weighted skills that are relevant for the specified role`
- `ischairslot.{$componentslot}` → `true if $componentslot is a NPC position slot aboard this object and related to a chair`
- `chairapproachslot.{$componentslot}` → `The approach slot of a NPC position slot related to a chair on this object`
- `chairbaseslot.{$componentslot}` → `The base chair slot of a NPC position slot related to a chair in this object. Used as a static anchor slot for the chair and can be used as a NPC waypoint.`
- `chairroomslot.{$componentslot}` → `The room slot related to a chair in this object, to be used by NPCs for destination reservation.`
- `controlposition.{$controlposition}.exists` → `true if a control position of the specified type exists on the controllable (where the room is virtual and does not have control positions)`
- `controlposition.{$controlposition}.roomslot` → `Slot which entities inhabit when working at the specified control position (where the room is virtual and does not have control positions)`
- `controlposition.{$controlposition}.entity` → `Entity currently working at the specified control position (where the room is virtual and does not have control positions)`
- `controlpositions.list` → `List of component slots which are control positions`
- `combinedskill` → `Effective combined skill value (from 0 to 100) of this controllable, taking entity and crew skill, where applicable, into account.`
- `canhaveplayercover` → `true if the controllable can have a cover owner when controlled by the player`
- `potentialplayercoverowner` → `Faction the controllable will cover as if player controls it and was to invoke cover`

## `defensible` — inherits `controllable` (225 direct properties)

- `iscapturable` → `Can this defensible be captured, either via signalleak (S/M sized) or via boarding (L+ sized). Additionally, for S-ships the pilot will not eject if it is not capturable`
- `isalertlevel.<alertlevel>` → `Is the defensible at the specfied alert level: red, yellow or green. Note: Turrets deactivate on alert level green.`
- `boardingoperation` → `The boarding operation this object is currently taking part in`
- `boardingoperations` → `List of the inbound boarding operations that this object is currently defending against`
- `boardingbehaviour` → `The boarding behaviour this object is assigned for its current operation`
- `boardingmarines.count` → `The total number of marines assigned from this ship for the boarding operation`
- `boardingmarines.combinedskill` → `The total marine related skill of all marines assigned from this ship for the boarding operation (between 0 and 100 per individual)`
- `boardingmarines.{$level}.count` → `The number of marines assigned from this ship for the boarding operation. Level is the marine tier skill value`
- `allmarinesdispatched` → `Have all marines set to join this this boarding operation been dispatched? (true if no marines have been assigned from this object)`
- `boardingresistance` → `Value of the total boarding resistance based on current state of the object and crew, including baseboardingresistance`
- `baseboardingresistance` → `Value of the base boarding resistance defined for this object`
- `boardingstrength` → `Value of boarding strength based on marines and marine officer`
- `constructionsequence` → `the current construction sequence of this object (or null if one doesn't exist)`
- `hasstagedconstruction` → `true if the current or planned construction sequence of this object has stages defined`
- `hasfutureconstructionstage` → `true if the current or planned construction sequence of this object is staged and has future stages`
- `planmodule.{$constructionplanentryid}` → `Contained module related to the provied construction plan entry`
- `requiresconstructionvessel.{constructionsequence}` → `true if the provided construction sequence will require a construction vessel`
- `defencedronemode` → `the current drone mode of defence drones of this defensible`
- `loadoutlevel` → `Loadout level used to generate this object`
- `rawloadoutlevel` → `Loadout level used to generate this object without fallback to parameters.xml. You need to check against -1 before using this.`
- `minloadoutlevel` → `The minimum allowed loadout level e.g. the lowerbound value defined in a job definition. Defaults to 0.`
- `loadoutvariation` → `The loadout variation range used to generate this object.`
- `moduleloadoutlevel` → `Module loadout level of this station`
- `rawmoduleloadoutlevel` → `Module loadout level of this station without fallback to parameters.xml. You need to check against -1 before using this.`
- `moduleloadoutvariation` → `Module loadout variation range used by this station.`
- `loadoutquantity.level` → `Loadout quantity level override used to generate this object`
- `loadoutquantity.variation` → `Loadout quantity variation override used to generate this object`
- `rawloadoutquantity.level` → `Loadout quantity level override used to generate this object without fallback to parameters.xml. You need to check against -1 before using this.`
- `rawloadoutquantity.variation` → `Loadout quantity variation override used to generate this object without fallback to parameters.xml. You need to check against -1 before using this.`
- `loadoutquality.level` → `Loadout quality level override used to generate this object`
- `loadoutquality.variation` → `Loadout quality variation override used to generate this object`
- `rawloadoutquality.level` → `Loadout quality level override used to generate this object without fallback to parameters.xml. You need to check against -1 before using this.`
- `rawloadoutquality.variation` → `Loadout quality variation override used to generate this object without fallback to parameters.xml. You need to check against -1 before using this.`
- `moduleloadoutquantity.level` → `Module loadout quantity level override of this station`
- `moduleloadoutquantity.variation` → `Module loadout quantity variation override of this station`
- `rawmoduleloadoutquantity.level` → `Module loadout quantity level override of this station without fallback to parameters.xml. You need to check against -1 before using this.`
- `rawmoduleloadoutquantity.variation` → `Module loadout quantity variation override  of this station without fallback to parameters.xml. You need to check against -1 before using this.`
- `moduleloadoutquality.level` → `Module loadout quality level override of this station`
- `moduleloadoutquality.variation` → `Module loadout quality variation override of this station`
- `rawmoduleloadoutquality.level` → `Module loadout quality level override of this station without fallback to parameters.xml. You need to check against -1 before using this.`
- `rawmoduleloadoutquality.variation` → `Module loadout quality variation override  of this station without fallback to parameters.xml. You need to check against -1 before using this.`
- `loadout` → `Current loadout of this object`
- `dps.all` → `Combined damage/second of all weapons and turrets. Ignores ammo usage.`
- `dps.primary` → `Combined damage/second of primary weapons. Ignores ammo usage.`
- `dps.secondary` → `Combined damage/second of secondary weapons. Ignores ammo usage.`
- `dps.lasers.all` → `Combined damage/second of primary and secondary laser weapons`
- `dps.lasers.primary` → `Combined damage/second of primary laser weapons`
- `dps.lasers.secondary` → `Combined damage/second of secondary laser weapons`
- `dps.missiles.all` → `Combined damage/second of primary and secondary missile weapons. Ignores ammo usage.`
- `dps.missiles.primary` → `Combined damage/second of primary missile weapons. Ignores ammo usage.`
- `dps.missiles.secondary` → `Combined damage/second of secondary missile weapons. Ignores ammo usage.`
- `dps.turrets.all` → `Combined damage/second of all turrets. Ignores ammo usage.`
- `dps.turrets.{$quadrant}` → `Combined damage/second of turrets in given quadrant. Ignores ammo usage.`
- `dps.turrets.<quadrantname>` → `Shortcut for dps.turrets.{quadrant.<quadrantname>}. Ignores ammo usage.`
- `dps.turrets.fortarget.{$object}.all` → `Combined damage/second of turrets suitable for given target. Ignores ammo usage.`
- `dps.turrets.fortarget.{$object}.{$quadrant}` → `Combined damage/second of turrets in given quadrant suitable for given target. Ignores ammo usage.`
- `dps.turrets.fortarget.{$object}.<quadrantname>` → `Shortcut for dps.turrets.fortarget.{$object}.{quadrant.<quadrantname>}. Ignores ammo usage.`
- `hasarmeddefencedrones` → `true if the defensible has defence drones and is authorized to use them`
- `hasarmedminingdrones` → `true if the defensible has mining drones and is authorized to use them`
- `hasarmedtransportdrones` → `true if the defensible has transport drones and is authorized to use them`
- `maxcombatrange.all` → `Maximum combat range of all weapons/turrets`
- `maxcombatrange.primary` → `Maximum weapon range of primary weapons`
- `maxcombatrange.secondary` → `Maximum weapon range of secondary weapons`
- `maxcombatrange.main.all` → `Maximum weapon range of primary and secondary laser and missile weapons`
- `maxcombatrange.main.primary` → `Maximum weapon range of primary laser and missile weapons`
- `maxcombatrange.main.secondary` → `Maximum weapon range of secondary laser and missile weapons`
- `maxcombatrange.lasers.all` → `Maximum weapon range of primary and secondary laser weapons`
- `maxcombatrange.lasers.primary` → `Maximum weapon range of primary laser weapons`
- `maxcombatrange.lasers.secondary` → `Maximum weapon range of secondary laser weapons`
- `maxcombatrange.missiles.all` → `Maximum weapon range of primary and secondary missile weapons`
- `maxcombatrange.missiles.primary` → `Maximum weapon range of primary missile weapons`
- `maxcombatrange.missiles.secondary` → `Maximum weapon range of secondary missile weapons`
- `maxcombatrange.turrets` → `Maximum range of all turrets`
- `maxcombatrange.{$weaponmode}.all` → `Maximum combat range of all weapons/turrets with the specified weapon mode`
- `maxcombatrange.{$weaponmode}.primary` → `Maximum combat range of primary weapons with the specified weapon mode`
- `maxcombatrange.{$weaponmode}.secondary` → `Maximum combat range of secondary weapons with the specified weapon mode`
- `maxcombatrange.{$weaponmode}.lasers.all` → `Maximum combat range of all weapons laser weapons with the specified weapon mode`
- `maxcombatrange.{$weaponmode}.lasers.primary` → `Maximum combat range of primary laser weapons with the specified weapon mode`
- `maxcombatrange.{$weaponmode}.lasers.secondary` → `Maximum combat range of secondary weapons with the specified weapon mode`
- `maxcombatrange.{$weaponmode}.missiles.all` → `Maximum combat range of all missile weapons with the specified weapon mode`
- `maxcombatrange.{$weaponmode}.missiles.primary` → `Maximum combat range of primary missile weapons with the specified weapon mode`
- `maxcombatrange.{$weaponmode}.missiles.secondary` → `Maximum combat range of secondary missile weapons with the specified weapon mode`
- `maxcombatrange.{$weaponmode}.turrets` → `Maximum range of all turrets with the specified weapon mode`
- `shortestmaxcombatrange.all` → `Shortest maximum combat range of all weapons/turrets`
- `shortestmaxcombatrange.primary` → `Shortest maximum weapon range of primary weapons`
- `shortestmaxcombatrange.secondary` → `Shortest maximum weapon range of secondary weapons`
- `shortestmaxcombatrange.lasers.all` → `Shortest maximum weapon range of primary and secondary laser weapons`
- `shortestmaxcombatrange.lasers.primary` → `Shortest maximum weapon range of primary laser weapons`
- `shortestmaxcombatrange.lasers.secondary` → `Shortest maximum weapon range of secondary laser weapons`
- `shortestmaxcombatrange.missiles.all` → `Shortest maximum weapon range of primary and secondary missile weapons`
- `shortestmaxcombatrange.missiles.primary` → `Shortest maximum weapon range of primary missile weapons`
- `shortestmaxcombatrange.missiles.secondary` → `Shortest maximum weapon range of secondary missile weapons`
- `shortestmaxcombatrange.turrets` → `Shortest maximum range of all turrets`
- `shortestmaxcombatrange.{$weaponmode}.all` → `Shortest maximum combat range of all weapons/turrets with the specified weapon mode`
- `shortestmaxcombatrange.{$weaponmode}.primary` → `Shortest maximum combat range of primary weapons with the specified weapon mode`
- `shortestmaxcombatrange.{$weaponmode}.secondary` → `Shortest maximum combat range of secondary weapons with the specified weapon mode`
- `shortestmaxcombatrange.{$weaponmode}.lasers.all` → `Shortest maximum combat range of all weapons laser weapons with the specified weapon mode`
- `shortestmaxcombatrange.{$weaponmode}.lasers.primary` → `Shortest maximum combat range of primary laser weapons with the specified weapon mode`
- `shortestmaxcombatrange.{$weaponmode}.lasers.secondary` → `Shortest maximum combat range of secondary weapons with the specified weapon mode`
- `shortestmaxcombatrange.{$weaponmode}.missiles.all` → `Shortest maximum combat range of all missile weapons with the specified weapon mode`
- `shortestmaxcombatrange.{$weaponmode}.missiles.primary` → `Shortest maximum combat range of primary missile weapons with the specified weapon mode`
- `shortestmaxcombatrange.{$weaponmode}.missiles.secondary` → `Shortest maximum combat range of secondary missile weapons with the specified weapon mode`
- `shortestmaxcombatrange.{$weaponmode}.turrets` → `Shortest maximum range of all turrets with the specified weapon mode`
- `miningdronemode` → `the current drone mode of mining drones of this defensible`
- `shields.numslots` → `Number of shield slots of this object`
- `shields.<state>.count` → `Number of shield generators of this object, filtered by component state: all, construction, operational or wreck`
- `shields.<state>.list` → `List of shield generators of this object, filtered by component state: all, construction, operational or wreck`
- `shields.<state>.indexof.{$component}` → `Index of $component in the list of shield generators of this object, filtered by component state (1-based), or 0 if not present`
- `shields.<state>.random` → `Random shield generator of this object, filtered by component state: all, construction, operational or wreck`
- `transportdronemode` → `the current drone mode of transport drones of this defensible`
- `turrets.numslots` → `Number of turret slots of this object`
- `turrets.<state>.count` → `Number of turrets of this object, filtered by component state: all, construction, operational or wreck`
- `turrets.<state>.list` → `List of turrets of this object, filtered by component state: all, construction, operational or wreck`
- `turrets.<state>.indexof.{$component}` → `Index of $component in the list of turrets of this object, filtered by component state (1-based), or 0 if not present`
- `turrets.<state>.random` → `Random turret of this object, filtered by component state: all, construction, operational or wreck`
- `missileturrets.<state>.count` → `Number of missile turrets of this object, filtered by component state: all, construction, operational or wreck`
- `missileturrets.<state>.list` → `List of missile turrets of this object, filtered by component state: all, construction, operational or wreck`
- `missileturrets.<state>.indexof.{$component}` → `Index of $component in the list of missile turrets of this object, filtered by component state (1-based), or 0 if not present`
- `missileturrets.<state>.random` → `Random missile turret of this object, filtered by component state: all, construction, operational or wreck`
- `weapons.numslots` → `Number of weapon slots of this object`
- `weapons.<state>.count` → `Number of weapons of this object, filtered by component state: all, construction, operational or wreck`
- `weapons.<state>.list` → `List of weapons of this object, filtered by component state: all, construction, operational or wreck`
- `weapons.<state>.indexof.{$component}` → `Index of $component in the list of weapons of this object, filtered by component state (1-based), or 0 if not present`
- `weapons.<state>.random` → `Random weapon of this object, filtered by component state: all, construction, operational or wreck`
- `primaryweapons.{$weapongroup}.count` → `Number of weapons of this object in this primary weapon group`
- `primaryweapons.{$weapongroup}.list` → `List of weapons of this object in this primary weapon group`
- `secondaryweapons.{$weapongroup}.count` → `Number of weapons of this object in this secondary weapon group`
- `secondaryweapons.{$weapongroup}.list` → `List of weapons of this object in this secondary weapon group`
- `modules.numslots` → `Number of module slots of this object`
- `modules.<state>.count` → `Number of modules of this object, filtered by component state: all, construction, operational or wreck`
- `modules.<state>.list` → `List of modules of this object, filtered by component state: all, construction, operational or wreck`
- `modules.<state>.indexof.{$component}` → `Index of $component in the list of modules of this object, filtered by component state (1-based), or 0 if not present`
- `modules.<state>.random` → `Random module of this object, filtered by component state: all, construction, operational or wreck`
- `units.list` → `List of macros of stored units`
- `units.table` → `Table of macros and amounts of stored units`
- `units.count` → `Number of stored units`
- `units.maxcount` → `Max number of stored units`
- `units.free` → `Amount of units that can still be stored`
- `units.collect.count` → `Number of stored collector units`
- `units.collect.{$ware}.count` → `Number of stored collector units suitable for given ware`
- `units.collect.{$ware}.list` → `List of stored collector unit macros suitable for given ware`
- `units.collect.{$ware}.table` → `Table of stored collector unit macros and amounts suitable for given ware`
- `units.collect.{$ware}.mk.{$i}.count` → `Number of stored collector units of given version suitable for given ware`
- `units.collect.{$ware}.mk.{$i}.list` → `List of stored collector unit macros of given version suitable for given ware`
- `units.collect.{$ware}.mk.{$i}.table` → `Table of stored collector unit macros of given version suitable for given ware`
- `units.{$macro}.count` → `Number of stored units of given macro`
- `units.{$unitcategory}.list` → `List of macros of stored units of given category`
- `units.{$unitcategory}.table` → `Table of macros and amounts of stored units of given category`
- `units.{$unitcategory}.count` → `Number of stored units of given category`
- `units.{$unitcategory}.mk.{$i}.count` → `Number of stored units of given category and version`
- `units.{$unitcategory}.mk.{$i}.list` → `List of macros of stored units of given category and version`
- `availableunits.list` → `List of macros of available units`
- `availableunits.table` → `Table of macros and amounts of available units`
- `availableunits.count` → `Number of available units`
- `availableunits.collect.count` → `Number of available collector units`
- `availableunits.collect.{$ware}.list` → `List of available collector unit macros suitable for given ware`
- `availableunits.collect.{$ware}.table` → `Table of available collector unit macros and counts suitable for given ware`
- `availableunits.collect.{$ware}.count` → `Number of available collector units suitable for given ware`
- `availableunits.collect.{$ware}.mk.{$i}.count` → `Number of available collector units of given version suitable for given ware`
- `availableunits.collect.{$ware}.mk.{$i}.list` → `List of available collector unit macros of given version suitable for given ware`
- `availableunits.{$macro}.count` → `Number of available units of given macro`
- `availableunits.{$unitcategory}.list` → `List of macros of available units of given category`
- `availableunits.{$unitcategory}.table` → `Table of macros and amounts of available units of given category`
- `availableunits.{$unitcategory}.count` → `Number of available units of given category`
- `availableunits.{$unitcategory}.mk.{$i}.count` → `Number of available units of given category and version`
- `availableunits.{$unitcategory}.mk.{$i}.list` → `List of macros of available units of given category and version`
- `ammostorage.missile.basecapacity` → `Base capacity of the defensible for this ammotype`
- `ammostorage.missile.capacity` → `Total capacity of the defensible for this ammotype`
- `ammostorage.missile.list` → `List of this ammotype currently stored for the defensible`
- `ammostorage.missile.table` → `Table of macros and amounts of this ammotype currently stored for the defensible`
- `ammostorage.missile.count` → `Amount of this ammotype currently stored for the defensible`
- `ammostorage.missile.free` → `Amount of this ammotype that can still be stored for the defensible`
- `ammostorage.countermeasure.basecapacity` → `Base capacity of the defensible for this ammotype`
- `ammostorage.countermeasure.capacity` → `Total capacity of the defensible for this ammotype`
- `ammostorage.countermeasure.list` → `List of this ammotype currently stored for the defensible`
- `ammostorage.countermeasure.table` → `Table of macros and amounts of this ammotype currently stored for the defensible`
- `ammostorage.countermeasure.count` → `Amount of this ammotype currently stored for the defensible`
- `ammostorage.countermeasure.free` → `Amount of this ammotype that can still be stored for the defensible`
- `ammostorage.deployable.basecapacity` → `Base capacity of the defensible for this ammotype (includes lasertowers, mines, satellites, navbeacons and resourceprobes)`
- `ammostorage.deployable.capacity` → `Total capacity of the defensible for this ammotype (includes lasertowers, mines, satellites, navbeacons and resourceprobes)`
- `ammostorage.deployable.list` → `List of this ammotype (includes lasertowers, mines, satellites, navbeacons and resourceprobes) currently stored for the defensible`
- `ammostorage.deployable.table` → `Table of macros and amounts of this ammotype (includes lasertowers, mines, satellites, navbeacons and resourceprobes) currently stored for the defensible`
- `ammostorage.deployable.count` → `Amount of this ammotype (includes lasertowers, mines, satellites, navbeacons and resourceprobes) currently stored for the defensible`
- `ammostorage.deployable.free` → `Amount of this ammotype (includes lasertowers, mines, satellites, navbeacons and resourceprobes) that can still be stored for the defensible`
- `ammostorage.{$deployablecategory}.list` → `List of macros of available deployables of given category`
- `ammostorage.{$deployablecategory}.table` → `Table of macros and amounts of available deployables of given category`
- `ammostorage.{$deployablecategory}.count` → `Number of available deployable of given category`
- `ammostorage.{$deployablecategory}.mk.{$i}.list` → `List of macros of available deployables of given category and version`
- `ammostorage.{$deployablecategory}.mk.{$i}.table` → `Table of macros and amounts of available deployables of given category and version`
- `ammostorage.{$deployablecategory}.mk.{$i}.count` → `Number of available deployables of given category and version`
- `ammostorage.{$macro}.count` → `Amount of this ammo macro currently stored for the defensible`
- `ammostorage.{$ware}.free` → `Amount of this ammo ware that can still be stored in the defensible`
- `isammocompatible.{$macro}` → `true iff the supplied ammo macro (missile) is compatible with the weapons on this defensible`
- `isenemylockingon` → `Whether an enemy is currently locking or locked on to this object`
- `ismissileincoming` → `Whether a missile is currently homing in on this object`
- `hasweaponmod` → `Whether the object has any weapon mod installed`
- `hasweaponmod.{$ware}` → `Whether the object has a weapon mod based on the specified weapon mod ware installed`
- `hasweaponmod.{$macro}` → `Whether the object has a weapon mod installed on a weapon of the specified macro`
- `hasweaponmod.{$macro}.{$ware}` → `Whether the object has a weapon mod based on the specified weapon mod ware installed on a weapon of the specified macro`
- `hasweaponmod.{$groupcontext}.{$grouptag}` → `Whether the object has a weapon mod installed on the specified weapon group (identified by macro path or component, and group tag)`
- `hasweaponmod.{$groupcontext}.{$grouptag}.{$ware}` → `Whether the object has a weapon mod based on the specified weapon mod ware installed on the specified weapon group (identified by macro path or component, and group tag)`
- `hasshieldmod` → `Whether the object has any shield mod installed on the object's main hull shield group`
- `hasshieldmod.{$ware}` → `Whether the object has a shield mod based on the specified shield mod ware installed on the object's main hull shield group`
- `hasshieldmod.{$groupcontext}.{$grouptag}` → `Whether the object has a shield mod installed on the specified shield group (identified by macro path or component, and group tag)`
- `hasshieldmod.{$groupcontext}.{$grouptag}.{$ware}` → `Whether the object has a shield mod based on the specified shield mod ware installed on the specified shield group (identified by macro path or component, and group tag)`
- `productions` → `List of all the contained production modules`
- `storagemodules` → `List of all the contained storage modules`
- `buildmodules` → `List of all the contained build modules`
- `processingmodules` → `List of all the contained processing modules`
- `dockareas` → `List of all the contained dock area modules`
- `piers` → `List of all the contained pier modules`
- `habitationmodules` → `List of all the contained habitation modules`
- `welfaremodules` → `List of all the contained welfare modules`
- `defencemodules` → `List of all the contained defence modules`
- `connectionmodules` → `List of all the contained connection modules`
- `buildmodule` → `A contained build module`
- `buildprocessor` → `A contained build processor`
- `buildprocessors` → `List of all the contained build processors`
- `freebuildprocessor` → `A contained free build processor`
- `freebuildprocessors` → `List of all the contained free build processors`
- `dismantletarget` → `The wreck assigned to be dismantled by this object`
- `isdismantlingassignedobject` → `Is this object currently dismantling the assigned wreck`
- `claimedsalvage` → `The object claimed as either a dismantle or tow target (other defensibles may also have claims)`
- `haswaveprotection` → `Is this object protected against the wave (taking current cargo into account if also a container)`
- `incomingmissilecount` → `Returns the number of guided missiles and torpedoes chasing this defensible`

## `container` — inherits `defensible` (110 direct properties)

- `hasmasstraffic` → `true iff the container is involved in the zone's mass-traffic network`
- `hasunitdrone.{$ship}` → `true if the container has the provided ship as drone unit`
- `istrafficlevel.<trafficlevel>` → `Is the container at the specified docking traffic level: normal, heavy or gridlock`
- `buildingmodule` → `The build module building this container`
- `buildingprocessor` → `The build processor building this container`
- `build` → `Build task constructing this object`
- `builds.queued` → `List of all the queued build tasks`
- `builds.inprogress` → `List of all build tasks in progress`
- `builds.todelete` → `List of all build tasks queued for deletion`
- `buildanchor` → `Build anchor`
- `buildequipment.wares` → `All equipment wares this object can build (= default items + included items - excluded items)`
- `buildequipment.absolute` → `Equipment wares that have been set as the absolute list of items this object can build (see <set_equipment_wares_absolute />)`
- `buildequipment.excluded` → `Equipment wares that have been excluded from the default items this object can build (see <set_equipment_wares_excluded />)`
- `buildequipment.included` → `Equipment wares that have been included on top of the default items this object can build (see <set_equipment_wares_included />)`
- `buildequipment.<type>` → `Equipment wares of the specified type which this object can build (respecting included/excluded wares of that type), see buildequipment types in buildmodule`
- `buildships.wares` → `All ship wares this object can build (= default items + included items - excluded items)`
- `buildships.absolute` → `Ship wares that have been set as the absolute list of items this object can build (see <set_ship_wares_absolute />)`
- `buildships.excluded` → `Ship wares that have been excluded from the default items this object can build (see <set_ship_wares_excluded />)`
- `buildships.included` → `Ship wares that have been included on top of the default items this object can build (see <set_ship_wares_included />)`
- `canbuildclass.{$class}` → `true iff this container has a build module capable of building objects of this class`
- `canequipclass.{$class}` → `true iff this container has a build module capable of equipping objects of this class`
- `cansupplyclass.{$class}` → `true iff this container has a build module capable of supplying objects of this class`
- `canbuildequipment.{$ware}` → `true iff this container has a build module capable of building this equipment`
- `canbuildequipment.{$list}` → `true iff this container has a build modules capable of building the equipment from this list (may be across multiple build modules)`
- `canbuildmacro.{$macro}` → `true iff this container has a build module capable of building this macro`
- `canbuildships` → `true iff this container can build ships (see also .isshipyard, .iswharf)`
- `canequipships` → `true iff this container can equip ships (see also .isequipmentdock)`
- `cansupplyships` → `true iff this container can supply ships (see also .issupplyship)`
- `canabortbuild.{$build}` → `true if the specified build can currently be aborted`
- `missingloadoutequipment.{$loadout}.{$faction}` → `Loadout equipment ware that this object is not allowed to construct`
- `buildresources.{$build}` → `Total resources for the specified build if built by this object (or the current remaining resources if the build is being processed by this object)`
- `buildresources.{$ship}` → `Total resources to build the specified ship if built by this object (or the current remaining resources if the ship is already under construction by this object)`
- `neededbuildresources.{$build}` → `Total missing resources for the specified build if built by this object (or the current missing remaining resources if the build is being processed by this object)`
- `neededbuildresources.{$ship}` → `Total missing resources for the specified ship if built by this object (or the current missing remaining resources if the ship is being processed by this object)`
- `hasplannedconstruction` → `true if there are plans to expand this object`
- `plannedconstruction.sequence` → `the planned construction sequence of this object (or current construction sequence is there is no queued build)`
- `plannedconstruction.boundingbox.exists` → `Whether the planned construction's bounding box has non-zero dimensions`
- `plannedconstruction.boundingbox.max` → `Maximum bounds of the planned construction's bounding box`
- `plannedconstruction.boundingbox.center` → `Center position of the planned construction's bounding box`
- `cargo` → `Wares in cargo`
- `cargo.{$ware}.target` → `Target amount for a traded commodity (product, resource or trade ware)`
- `products` → `All produced wares (including intermediate wares)`
- `research` → `All research wares currently being worked on by this container`
- `dockingenabled` → `Is docking at the container enabled`
- `dockingallowed.{$ship}` → `Is ship allowed to dock at the container`
- `products.{$ware}.intermediate` → `true iff $ware is an intermediate ware`
- `originalproduct` → `The ware that the container identifies as its original product`
- `resources` → `All resource wares (including intermediate wares)`
- `resources.pure` → `All resource wares which are not intermediate wares`
- `resources.intermediate` → `All intermediate resource wares`
- `resources.primary` → `All primary resource wares (including intermediate wares)`
- `resources.secondary` → `All secondary resource wares (including intermediate wares)`
- `resources.{$ware}.intermediate` → `true iff $ware is an intermediate ware`
- `resources.{$ware}.primary` → `true iff $ware is a primary resource`
- `resources.{$ware}.secondary` → `true iff $ware is a secondary resource`
- `supplyresources` → `All resource wares required for supplying units and ammunition of $container. Note that this does not include production resources. Includes inbound reserved wares.`
- `tradewares` → `All trade wares (wares that are bought/sold at the container but are neither product nor resource)`
- `buyprices` → `Table of the current buy prices for all wares relevent to this container`
- `sellprices` → `Table of the current sell prices for all wares relevent to this container`
- `buildbuyprices` → `Table of the current buy prices for all wares relevent to this container, accounting for 'buildpricefactor'`
- `buildsellprices` → `Table of the current sell prices for all wares relevent to this container, accounting for 'buildpricefactor'`
- `buyprice.{$ware}` → `Current buy price for the specified ware`
- `sellprice.{$ware}` → `Current sell price for the specified ware`
- `buildprice.{$ware}` → `Current cost of resources to build the specified ware`
- `buypriceoverride.{$ware}` → `Current buy price override for the specified ware (0Cr if there is no price override for this ware)`
- `sellpriceoverride.{$ware}` → `Current sell price override for the specified ware (0Cr if there is no price override for this ware)`
- `referenceprice.{$ware}` → `Current trade reference price for the specified ware (0Cr if there is no reference price for this ware)`
- `referenceprofit.{$ware}.{$price}.{$amount}` → `Current trade reference profit for the specified ware given the specified sale price and amount to sell (0Cr if there is no reference price for this ware)`
- `waretransport` → `List of waretransport types which can be carried by this object`
- `productionmoney` → `amount of money wanted to maintain a minimum stocklevel of resources for production (not subtracting current account)`
- `wantedmoney` → `amount of money wanted to buy all remaining resources for construction (not subtracting current account)`
- `istraderestricted` → `true iff container can only trade with its owner faction (global setting)`
- `istraderestricted.{$ware}` → `true iff container can only trade this ware with its owner faction`
- `hastradesubscription` → `true iff player is currently getting trade offer updates of this object, no matter how these updates are unlocked`
- `haspermanenttradesubscription` → `true iff player has a permanent subscription to trade offer updates of this object`
- `supplies` → `List of all wares in supply storage`
- `supplyorders` → `List of all items (ammo/drones) that have been ordered`
- `workforce.{$race}.amount` → `Amount of workforce of the specified race (may be null)`
- `workforce.{$race}.capacity` → `Capacity for workforce of the specified race (may be null)`
- `workforce.races` → `List of workforce races which this container can currently have`
- `workforce.amount` → `Amount of workforce not tied to a specific race`
- `workforce.amounts` → `Table mapping race to current amount of workforce for that race (only races for which there are habitation modules are listed)`
- `workforce.capacity` → `Capacity for workforce not tied to a specific race`
- `workforce.capacities` → `Table mapping race to capacity of workforce for that race (only races for which there are habitation modules are listed)`
- `workforce.bonus` → `Bonus gained from workforce`
- `workforce.optimal` → `Number of workers required for object to operate at peak efficiency`
- `workforce.min` → `Number of workers required for object to operate`
- `money` → `Money in the container's account`
- `hasownaccount` → `true iff container has its own account`
- `isaccountholder` → `true iff container has a budget or is its own account holder`
- `minbudget` → `Min budget defined for the container`
- `maxbudget` → `Max budget defined for the container`
- `buildpricefactor` → `Additional factor applied to price for building ships (based on build queue size)`
- `isbuildrestricted.{$faction}` → `true iff container cannot build for this faction (deprecated but kept for compatibility, prefer using .maybuildfor.{$faction})`
- `hasresourcesfor.{$ware}` → `true iff container can produce or build, and has enough resources to produce or build the ware`
- `hasresourcesfor.{$table}` → `true iff container can produce or build, and has enough resources to produce or build all of the wares in the amounts specified. $table is a table that maps wares to corresponding amounts.`
- `maybesuppliedby.{$faction}` → `true iff container is allowed to be supplied by this faction`
- `maybesuppliedby.[$faction, $ware]` → `true iff container is allowed to be supplied with ware by this faction`
- `maybuyfrom.{$faction}` → `true iff container is allowed to buy from this faction`
- `maybuyfrom.[$faction, $ware]` → `true iff container is allowed to buy ware from this faction`
- `maybuildfor.{$faction}` → `true iff container is allowed to build for this faction`
- `maysellto.{$faction}` → `true iff container is allowed to sell to this faction`
- `maysellto.[$faction, $ware]` → `true iff container is allowed to sell ware to this faction`
- `maytransmutefor.{$faction}` → `true iff container is allowed to transmute resources when building for this faction`
- `tradewaremoney` → `amount of money wanted to maintain full target amounts of trade-only wares (not subtracting current account and ignoring existing cargo)`
- `spawntime` → `the gametime when this object was created or connected to the universe`
- `age` → `how long ago this object was created or connected to the universe`
- `iscontrolpanelhacked.{$controlpaneltype}` → `true iff the container has at least one hacked control panel of the specified type`
- `dock.{$docksize}` → `Suitable dock for this docksize available to this container (can be occupied)`
- `freedock.{$docksize}` → `Suitable free dock for this docksize available to this container`

## `ship` — inherits `container` (71 direct properties)

- `type` → `Ship type`
- `typename` → `Ship type name`
- `numfreeactorslots` → `Number of free actor slots (deprecated, always returns 0)`
- `actors` → `List of actors on the ship`
- `assigneddock` → `Dock currently assigned to this ship`
- `docksize` → `Tag of required dock size`
- `dock` → `Dock where this ship is docked`
- `dockslot` → `Slot on the ship to which docking bay connects when ship is docked`
- `todockposition.{$dockingbay}` → `The positional offset to the forward facing todock position relative to the ship's current position`
- `todockrotation.{$dockingbay}` → `The rotational offset to the forward facing todock position relative to the ship's current orientation`
- `todockpositionreverse.{$dockingbay}` → `The positional offset to the backwards facing todock position relative to the ship's current position`
- `todockrotationreverse.{$dockingbay}` → `The rotational offset to the backwards facing todock position relative to the ship's current orientation`
- `hidecargochance` → `Chance that illegal or valuable cargo on board is successfully hidden from scans (0-100, higher is better)`
- `maxspeed` → `Maximum speed with present engine set up and conditions (in m/s)`
- `unboostedmaxspeed` → `Maximum unboosted (i.e. non-travel and non-boost) speed with present engine set up and conditions (in m/s)`
- `maxyawspeed` → `Maximum rate of change in yaw with present engine set up and conditions (in rad/s)`
- `maxpitchspeed` → `Maximum rate of change in pitch with present engine set up and conditions (in rad/s)`
- `maxrollspeed` → `Maximum rate of change in roll with present engine set up and conditions (in rad/s)`
- `speedlimit` → `The speed limit currently imposed by the ship's environment (in m/s, -1 if there is none)`
- `canenterhighway` → `true iff this ship is capable of entering highways`
- `parkedat` → `Tradeoffer component that this ship is parked at (= has parking connection to)`
- `pickedupobject` → `The object which is currently being carried by this ship`
- `regiondamageprotection` → `Amount of protection against static environmental damage (0-100, higher is better)`
- `job` → `job ID`
- `jobname` → `job name`
- `isjobship` → `true if this is a job ship`
- `isvalidjobship` → `true if this is a job ship who's place in their command heirarchy is valid according to their job definition`
- `iswaitingjobship` → `true if this is a job ship which is not yet initialised to be an active ship (may not yet be connected to the universe)`
- `isrequestedjobship` → `true if this is a requested job ship`
- `jobexpired` → `true if this is a non-commandeered job ship which has passed its expiration time`
- `jobloadoutfaction` → `faction explicitly defined for this job ship to generate its loadout with, otherwise the current true owner`
- `jobcommander` → `the original ship which this ship was set to call commander (may have changed)`
- `jobmainsector` → `the sector this ship is set to perform in or start from`
- `jobmainzone` → `the zone this ship is set to perform in or start from`
- `isvalidjobspace.{$space}` → `is the provided space currently valid according to the job definition of this ship`
- `jobsubordinates.valid` → `List of subordinates who's place in the hierarchy is valid according to the job definition of this ship`
- `jobsubordinates.invalid` → `List of subordinates who's place in the hierarchy is not valid according to the job definition of this ship`
- `encounterid` → `Encounter type ID defined by this ship's job`
- `isencountership` → `true if this is a ship for encounters`
- `warebasket` → `Wares in job ship basket`
- `constructionmodule` → `Build module which this construction vessel is assigned to be deployed at`
- `isdeployedconstructionvessel` → `true if this ship is a construction vessel currently deployed at their 'constructionmodule'`
- `iscapitalship` → `true if this is a capital ship (size L or XL)`
- `islasertower` → `true iff the ship is a lasertower`
- `canhaveattackablemodules` → `true iff the ship is defined to contain a defence module which indicates it may have targetable modules`
- `hasshipmod` → `Whether the object has any ship mod installed`
- `hasshipmod.{$ware}` → `Whether the object has a ship mod based on the specified ship mod ware installed`
- `canbeclaimed` → `Whether the ship is currently in a claimable state`
- `defaultformationradius.{$ship}` → `The appropriate formation radius for this ship and its formation leader($ship)`
- `issupplyship` → `true if this ship is capable of re-supplying other ships, i.e. it can repair ships and equipment or produce ammo/units (see also .cansupplyships) but cannot build equipment or ships from scratch`
- `movementrefobject` → `The object this ship is currently moving relative to`
- `activeweapongroup.primary` → `The currently active primary weapon group`
- `activeweapongroup.secondary` → `The currently active secondary weapon group`
- `environment` → `Component which this ship is currently physically inside, but not necessarily connected to (limited to specific components, usually dock areas and build modules)`
- `cantowobjects` → `true iff this ship is capable of towing objects`
- `towedobject` → `the object this ship is towing`
- `takesregiondamage` → `true if this ship is susceptible to region damage`
- `diplomacy.agent` → `The agent this ship is assigned to for assisting in diplomacy actions`
- `stances.active` → `The ID string of the currently active ship stance (can be null)`
- `stances.default` → `The ID string of the default ship stance (can be null)`
- `stances.list` → `List of supported ship stances (ID strings)`
- `stances.count` → `Number of supported ship stances`
- `stances.random` → `The ID string of a random supported ship stance`
- `stances.unlocktime` → `Earliest game time at which ship stance switching is allowed`
- `stances.canswitch` → `Whether ship stance switching is allowed at the current time`
- `stances.{$list}` → `Ship stance that matches all listed tags`
- `madscore.isexceedingmax` → `Whether the ship's MAD score is exceeding the maximum`
- `madscore.value` → `Returns the current MAD score`
- `traveldrivestability.maxvalue` → `Maximum amount of Travel Drive Stability hitpoints this ship can have. A value of -1 makes the ship's Travel Drive uninterruptable. A value of 0 makes it stop for any kind of damage.`
- `traveldrivestability.remainingresettime` → `Returns the remaining Travel Drive Stability time until next reset`
- `traveldrivestability.value` → `The current amount of Travel Drive Stability hitpoints that an attacker needs to eliminate to disrupt the target's travel drive`

## `spacesuit` — inherits `ship` (4 direct properties)

- `oxygenempty` → `Is the spacesuit empty of oxygen`
- `oxygenlow` → `Is the spacesuit low on oxygen`
- `oxygenpercentage` → `Percentage of remaining oxygen supply`
- `oxygentimeremaining` → `Remaining time until oxygen is depleted`

## `station` — inherits `container` (26 direct properties)

- `buildplot.exists` → `Whether station's build plot has non-zero dimensions`
- `buildplot.max` → `Maximum bounds of station's build plot`
- `buildplot.center` → `Center position of station's build plot`
- `buildplot.price` → `The licence price for this build plot at the station's location`
- `paidbuildplot.exists` → `Whether station's build plot licenced by the player has non-zero dimensions`
- `paidbuildplot.max` → `Maximum bounds of station's build plot licenced by the player`
- `paidbuildplot.center` → `Center position of station's build plot licenced by the player`
- `paidbuildplot.payment` → `Amount the player paid for the current build plot licence`
- `paidbuildplot.haspositionchanged` → `Whether the station's position has changed since the build plot was licenced`
- `buildstorage` → `Build storage of the station`
- `canhavebuildstorage` → `true if this station is supposed to have a build storage`
- `istradestation` → `true if this station is a trade station`
- `isshipyard` → `true if this station is a shipyard, i.e. it can build capital ships (see also .canbuildships)`
- `iswharf` → `true if this station is a wharf, i.e. it can build non-capital ships (see also .canbuildships)`
- `isequipmentdock` → `true if this station is an equipment dock, i.e. it can change loadouts (see also .canequipships) but cannot build ships from scratch`
- `isdefencestation` → `true if this station is a defence station`
- `isrecyclingfacility` → `true if this station is a recycling facility with a processing module`
- `ispiratebase` → `true if this station is a pirate base`
- `isheadquarters` → `true if this station macro is tagged as a headquarters. Normally only true for the Player HQ.`
- `isfactionheadquarters` → `true if this station is a faction headquarters`
- `isplannedshipyard` → `true if this station is set to be a shipyard when fully constructed, i.e. it can build capital ships (see also .canbuildships)`
- `isplannedwharf` → `true if this station is set to be a wharf when fully constructed, i.e. it can build non-capital ships (see also .canbuildships)`
- `isplannedequipmentdock` → `true if this station is set to be an equipment dock, when fully constructed, i.e. it can change loadouts (see also .canequipships) but cannot build ships from scratch`
- `isplanneddefencestation` → `true if this station is set to be a defence station, when fully constructed`
- `isplannedrecyclingfacility` → `true if this station is set to be a recycling facility with a processing module, when fully constructed`
- `isscheduledfordeconstruction` → `true if this station is scheduled to be fully deconstructed`

## `explosive` — inherits `object` (4 direct properties)

- `istargetable` → `true if this explosive is targetable`
- `isguided` → `true if this explosive is guided`
- `istorpedo` → `true if this explosive is a torpedo`
- `countermeasureresistance.{$macro}` → `percentage change of this explosive resisting the effects of the provided countermeasure macro`

## `anomaly` — inherits `object` (3 direct properties)

- `destinations` → `List of destination anomalies this anomaly can lead to`
- `istransitiondestination` → `Is anomaly a valid destination for transitions from other anomalies`
- `istransitionsource` → `Is anomaly a valid source for transitions to other anomalies`

## `bullet` — inherits `component` (1 direct properties)

- `launcher` → `Weapon that fired this bullet`

## `missile` — inherits `explosive` (4 direct properties)

- `target` → `Missile target`
- `launcher` → `Object that launched this missile`
- `isswarm` → `true if this is a swarm missile`
- `isdistributing` → `true if this is a swarm missile that distributes its attack across multiple targets`

## `gate` — inherits `object` (6 direct properties)

- `destination` → `Destination zone`
- `exit` → `Destination gate`
- `isaccelerator` → `Is gate a trans-orbital accelerator`
- `entryhighway` → `Highway which leads into this gate`
- `exithighway` → `Highway which this gate leads into`
- `waitingship` → `Ship that has currently reserved the gate`

## `highwayentrygate` — inherits `object` (4 direct properties)

- `highway` → `Associated highway`
- `destination` → `Highway destination zone`
- `exit` → `Highway exit gate`
- `waitingship` → `Ship that has currently reserved the gate`

## `highwayexitgate` — inherits `object` (2 direct properties)

- `highway` → `Associated highway`
- `entry` → `Highway entry gate`

## `checkpoint` — inherits `object` (1 direct properties)

- `sequence` → `Sequence number of checkpoint`

## `datavault` — inherits `object` (3 direct properties)

- `islocked` → `Is the data vault fully locked`
- `ispartiallyunlocked` → `Is the data vault partially unlocked`
- `isunlocked` → `Is the data vault fully unlocked`

## `drop` — inherits `object` (0 direct properties)


## `satellite` — inherits `object` (1 direct properties)

- `isadvanced` → `Is an advanced satellite`

## `navbeacon` — inherits `object` (0 direct properties)


## `resourceprobe` — inherits `object` (2 direct properties)

- `currentyield` → `The current total yield detected by the resource probe (volume is a cube of space with a side length of 32km)`
- `bestyieldrating.{$ware}` → `The best yield rating for this ware detected by the resource probe (0 to 15)`

## `lockbox` — inherits `object` (6 direct properties)

- `rarity` → `Rarity of the lockbox`
- `locks.<state>.count` → `Number of locks on this lockbox, filtered by component state: all, construction, operational or wreck`
- `locks.<state>.list` → `List of locks on this lockbox, filtered by component state: all, construction, operational or wreck`
- `locks.<state>.random` → `Random lock on this lockbox, filtered by component state: all, construction, operational or wreck`
- `timeline` → `Contained timeline entry ids`
- `audiologs` → `Contained audiolog entry ids`

## `lock` — inherits `destructible` (0 direct properties)


## `collectable` — inherits `drop` (0 direct properties)


## `collectableammo` — inherits `collectable` (2 direct properties)

- `ammo.count` → `Amount of the contained ammo`
- `ammo.macro` → `Macro of the contained ammo`

## `collectablewares` — inherits `collectable` (3 direct properties)

- `money` → `Contained money`
- `unbundle` → `true iff the crate is flagged for converting its wares into ammo/units on pickup`
- `isdroppedcontainer` → `true iff the collectable is a dropped container (and not an asteroid chunk or some other type of collectable natural object in space)`

## `collectableblueprints` — inherits `collectable` (1 direct properties)

- `blueprints` → `Contained blueprints`

## `collectabledata` — inherits `collectable` (2 direct properties)

- `timeline` → `Contained timeline entry ids`
- `audiologs` → `Contained audiolog entry ids`

## `buildstorage` — inherits `container` (2 direct properties)

- `base` → `Base station of the build storage`
- `isscheduledfordeconstruction` → `true if the base station is scheduled to be fully deconstructed`

## `adsign` — inherits `destructible` (0 direct properties)


## `shieldgenerator` — inherits `destructible` (0 direct properties)


## `navcontext` — inherits `destructible` (3 direct properties)

- `ispersistent` → `Is the navcontext is set to be persistent? If true, the interior can exist in low attentions.`
- `isprivate` → `Is the navcontext is set to private? If true, contained NPC slots can only be found by directly querying the contained rooms`
- `rooms` → `Contained rooms of the navcontext`

## `module` — inherits `destructible` (2 direct properties)

- `numdocks.{$docksize}` → `Number of connected dockingbays supporting the specified docksize`
- `haswalkableroom` → `Does module contain any walkable rooms, i.e. accessible to the player and NPCs? This can be false e.g. for dock areas with only docking bays in space or in internal storage`

## `buildmodule` — inherits `walkablemodule` (50 direct properties)

- `buildprocessor` → `A contained build processor`
- `buildprocessors` → `List of all the contained build processors`
- `freebuildprocessor` → `A contained free build processor`
- `freebuildprocessors` → `List of all the contained free build processors`
- `isbusy` → `true iff all build processors are building`
- `isbuilding` → `true iff any build processor is building`
- `canbuildclass.{$class}` → `true iff this build module is capable of building objects of this class`
- `canequipclass.{$class}` → `true iff this build module is capable of equipping objects of this class`
- `cansupplyclass.{$class}` → `true iff this build module is capable of supplying objects of this class`
- `canbuildequipment.{$ware}` → `true iff this build module is capable of building this equipment`
- `canbuildequipment.{$list}` → `true iff this build modules is capable of building the equipment from this list`
- `canbuildmacro.{$macro}` → `true iff this build module is capable of building this macro`
- `buildequipment.wares` → `All equipment wares the build module's container can build (= default items + included items - excluded items)`
- `buildequipment.absolute` → `Equipment wares that have been set as the absolute list of items this build module's container can build (see <set_equipment_wares_absolute />)`
- `buildequipment.excluded` → `Equipment wares that have been excluded from the default items this build module's container can build (see <set_equipment_wares_excluded />)`
- `buildequipment.included` → `Equipment wares that have been included on top of the default items this build module's container can build (see <set_equipment_wares_included />)`
- `buildequipment.countermeasures` → `Countermeasure equipment wares the build module's container can build (respecting included/excluded wares of that type)`
- `buildequipment.drones` → `Drone equipment wares the build module's container can build (respecting included/excluded wares of that type)`
- `buildequipment.engines` → `Engine equipment wares the build module's container can build (respecting included/excluded wares of that type)`
- `buildequipment.lasertowers` → `Lasertower equipment wares the build module's container can build (respecting included/excluded wares of that type)`
- `buildequipment.mines` → `Mine equipment wares the build module's container can build (respecting included/excluded wares of that type)`
- `buildequipment.missiles` → `Missile equipment wares the build module's container can build (respecting included/excluded wares of that type)`
- `buildequipment.navbeacons` → `NavBeacon equipment wares the build module's container can build (respecting included/excluded wares of that type)`
- `buildequipment.resourceprobes` → `ResourceProbe equipment wares the build module's container can build (respecting included/excluded wares of that type)`
- `buildequipment.satellites` → `Satellite equipment wares the build module's container can build (respecting included/excluded wares of that type)`
- `buildequipment.shields` → `Shield equipment wares the build module's container can build (respecting included/excluded wares of that type)`
- `buildequipment.software` → `Software equipment wares the build module's container can build (respecting included/excluded wares of that type)`
- `buildequipment.thrusters` → `Thruster equipment wares the build module's container can build (respecting included/excluded wares of that type)`
- `buildequipment.turrets` → `Turret equipment wares the build module's container can build (respecting included/excluded wares of that type)`
- `buildequipment.weapons` → `Weapon equipment wares the build module's container can build (respecting included/excluded wares of that type)`
- `buildships.wares` → `All ship wares the build module's container can build, filtered by the allowed classes for this build module (= default items + included items - excluded items)`
- `buildships.absolute` → `Ship wares that have been set as the absolute list of items this build module's container can build (see <set_equipment_wares_absolute />)`
- `buildships.excluded` → `Ship wares that have been excluded from the default items this build module's container can build (see <set_equipment_wares_excluded />)`
- `buildships.included` → `Ship wares that have been included on top of the default items this build module's container can build (see <set_equipment_wares_included />)`
- `buildmacros` → `List of macros the build module can build`
- `buildanchor` → `Build anchor`
- `constructingcomponents` → `List of all components under construction by build processors of this build module`
- `constructingmodule` → `Module currently under construction by this build module`
- `buildstorage` → `Build storage of the build module`
- `requiresconstructionvessel` → `true if any build processor build will require a construction vessel to begin once other requirements are made`
- `mayrequireconstructionvessel` → `true if the any current or queued builds of a build processor may be in need of a construction vessel (this is a tentative result and .requiresconstructionvessel may return a different result as builds progress)`
- `iswaitingforconstructionvessel` → `true if any build processor is currently waiting for a construction vessel to start a build (usually meaning that it has enough resources/storage to start)`
- `iswaitingforresources` → `true if any build processor is currently waiting for resources to start a build`
- `iswaitingforstorage` → `true if any build processor is currently waiting for storage to start recycling`
- `constructionvessel` → `Deployed construction vessel for this build module`
- `constructionvesseldeployed` → `true iff the construction vessel is currently deployed at the build module`
- `dock.{$docksize}` → `Suitable dock for this docksize available to this build module (can be occupied)`
- `freedock.{$docksize}` → `Suitable free dock for this docksize available to this build module`
- `buildresources.{$build}` → `Total resources for the specified build if built by this module (or the current remaining resources if the build is being processed by this build module)`
- `neededbuildresources.{$build}` → `Total missing resources for the specified build if built by this module (or the current missing remaining resources if the build is being processed by this build module)`

## `buildprocessor` — inherits `component` (40 direct properties)

- `buildmodule` → `build module containing this build processor`
- `isbusy` → `true iff building`
- `isbuilding` → `true iff building`
- `elapsedtime` → `Elapsed time`
- `elapsedsteptime` → `Elapsed step time`
- `steptime` → `Step time`
- `totaltime` → `Total time`
- `canabortbuild` → `true if this build processor's current build is in an abortable state`
- `canbuildclass.{$class}` → `true iff this build processor's build module is capable of building objects of this class`
- `canequipclass.{$class}` → `true iff this build processor's build module is capable of equipping objects of this class`
- `cansupplyclass.{$class}` → `true iff this build processor's build module is capable of supplying objects of this class`
- `canbuildequipment.{$ware}` → `true iff this build processor's build module is capable of building this equipment`
- `canbuildequipment.{$list}` → `true iff this build processor's build modules is capable of building the equipment from this list`
- `canbuildmacro.{$macro}` → `true iff this build processor's build module is capable of building this macro`
- `buildequipment.wares` → `All equipment wares the build processor's container can build (= default items + included items - excluded items)`
- `buildequipment.absolute` → `Equipment wares that have been set as the absolute list of items this build processor's container can build (see <set_equipment_wares_absolute />)`
- `buildequipment.excluded` → `Equipment wares that have been excluded from the default items this build processor's container can build (see <set_equipment_wares_excluded />)`
- `buildequipment.included` → `Equipment wares that have been included on top of the default items this build processor's container can build (see <set_equipment_wares_included />)`
- `buildequipment.<type>` → `Equipment wares of the specified type which the build processor's container can build (respecting included/excluded wares of that type), see buildequipment types in buildmodule`
- `buildships.wares` → `All ship wares the build processor's container can build, filtered by the allowed classes for this build processor's build module (= default items + included items - excluded items)`
- `buildships.absolute` → `Ship wares that have been set as the absolute list of items this build processor's container can build (see <set_equipment_wares_absolute />)`
- `buildships.excluded` → `Ship wares that have been excluded from the default items this build processor's container can build (see <set_equipment_wares_excluded />)`
- `buildships.included` → `Ship wares that have been included on top of the default items this build processor's container can build (see <set_equipment_wares_included />)`
- `buildmacros` → `List of macros the build processor's build module can build`
- `buildanchor` → `Build anchor`
- `constructingcomponents` → `List of all components under construction by this build processor`
- `constructingmodule` → `Module currently under construction by this build processor`
- `build` → `Current build task of this build processor`
- `queuedbuild` → `Queued build task of this build processor`
- `requiresconstructionvessel` → `true if the current build will require a construction vessel to begin once other requirements are made`
- `mayrequireconstructionvessel` → `true if the current or queued build may be in need of a construction vessel (this is a tentative result and .requiresconstructionvessel may return a different result as builds progress)`
- `iswaitingforconstructionvessel` → `true if the current build is currently waiting for a construction vessel to start a build (usually meaning that it has enough resources/storage to start)`
- `iswaitingforresources` → `true if the build processor is currently waiting for resources to start a build`
- `iswaitingforstorage` → `true if the build processor is currently waiting for storage to start recycling`
- `currentslotresources` → `Total resources for the current build`
- `stepresources` → `Resources needed per step of the build, excluding the final step which requires .laststepresources`
- `laststepresources` → `Resources needed for the last step of the build (may differ from .stepresources due to rounding)`
- `neededslotresources` → `Resources needed for the current build`
- `neededsequenceresources` → `Resources needed for the whole sequence of builds`
- `recycled` → `Resources recycled during this sequence of builds`

## `connectionmodule` — inherits `module` (1 direct properties)

- `isventuremodule` → `true if this module is for use with venture platforms`

## `defencemodule` — inherits `module` (0 direct properties)


## `ventureplatform` — inherits `module` (2 direct properties)

- `venturedocks` → `List of venture docks associated with this venture module`
- `ventureships` → `List of venture ships associated with this venture module`

## `habitationmodule` — inherits `module` (5 direct properties)

- `workforce.capacity` → `Capacity for workforce`
- `workforce.race` → `Race of the workforce`
- `resources` → `All resource wares`
- `resources.{$ware}.primary` → `true iff $ware is a primary resource`
- `resources.{$ware}.secondary` → `true iff $ware is a secondary resource`

## `welfaremodule` — inherits `module` (0 direct properties)


## `pier` — inherits `module` (1 direct properties)

- `numpierdocks` → `Number of connected capital ship dock locations`

## `production` — inherits `module` (10 direct properties)

- `isproducing` → `true iff producing`
- `ispaused` → `true iff paused for any reason (hacked, manually, damaged...)`
- `ispausedmanually` → `true iff paused manually (see also: <set_production_paused />)`
- `iswaitingforresources` → `true if the production module is currently waiting for resources to start`
- `iswaitingforstorage` → `true if the production module is currently waiting for storage space for products`
- `products` → `All produced wares`
- `research` → `All research wares currently being worked on by this module`
- `resources` → `All resource wares`
- `resources.{$ware}.primary` → `true iff $ware is a primary resource`
- `resources.{$ware}.secondary` → `true iff $ware is a secondary resource`

## `processingmodule` — inherits `module` (5 direct properties)

- `furnacestartpos` → `Position on module near which an object should be before calling <process_recyclable>`
- `products` → `All produced wares`
- `resources` → `All resource wares`
- `resources.{$ware}.primary` → `true iff $ware is a primary resource`
- `resources.{$ware}.secondary` → `true iff $ware is a secondary resource`

## `storagemodule` — inherits `module` (2 direct properties)

- `cargo` → `Wares in cargo`
- `waretransport` → `List of waretransport types which can be carried by this module`

## `engine` — inherits `destructible` (13 direct properties)

- `boost.available` → `true iff the booster can be activated right now`
- `boost.active` → `true iff the booster is currently active`
- `boost.chargetime` → `Charge time until the boost starts`
- `boost.rechargetime` → `Time required to recharge after a boost`
- `boost.maxduration` → `The maximum boost duration possible`
- `boost.remainingduration` → `Currently remaining boost duration until energy is depleted (in s)`
- `boost.remainingfraction` → `Currently remaining fraction of boost energy (value from 0 to 1)`
- `boost.maxspeed` → `Maximum boost speed with present engine set up and conditions (in m/s)`
- `travel.available` → `true iff the engine's travel mode can be activated right now`
- `travel.active` → `true iff the engine is currently traveling`
- `travel.chargetime` → `The time in seconds until travel mode actually starts`
- `travel.maxspeed` → `Maximum travel speed with present engine set up and conditions (in m/s)`
- `travel.iscoasting` → `true iff the engine is currently coasting after turning off travel mode`

## `scanner` — inherits `destructible` (0 direct properties)


## `crate` — inherits `destructible` (3 direct properties)

- `money` → `Contained money`
- `timeline` → `Contained timeline entry ids`
- `audiologs` → `Contained audiolog entry ids`

## `controlpanel` — inherits `destructible` (2 direct properties)

- `type` → `Control panel type`
- `requireditems` → `Required items for hacking`

## `signalleak` — inherits `component` (2 direct properties)

- `type` → `Signal leak type`
- `islocked` → `Is the signal leak locked`

## `room` — inherits `component` (26 direct properties)

- `type` → `Room type`
- `islocked` → `Is the room locked`
- `isgrouplocked.{$grouptag}` → `Is the specified grouptag in this room locked`
- `isprivate` → `Is the room in a dynamic interior which is set to be private. If true, contained NPC slots can only be found by directly querying the room`
- `iswalkable` → `Is the room walkable, i.e. accessible to the player and NPCs? This can be false e.g. for docking bays in space or in internal storage`
- `iscurrentlywalkable` → `Is the room currently walkable for the player and NPCs? Can be temporarily false for animated rooms or if the navigation mesh is not yet ready.`
- `haswalkableroom` → `Is the room, or any of the rooms it contains, walkable, i.e. accessible to the player and NPCs? This can be false e.g. for docking bays in space or in internal storage`
- `dockarea` → `The dock area this room is a part of`
- `buildmodule` → `The build module this room is a part of`
- `walkablemodule` → `The walkable module (dock area or build module) this room is a part of`
- `dynamicinterior` → `The dynamic interior this room is a part of`
- `actors` → `List of actors in the room`
- `slotactor.{$componentslot}` → `Actor reserved for the specified NPC slot or related chair slots`
- `waypointactors.{$componentslot}` → `List of entities currently moving towards the specified NPC waypoint`
- `numfreeactorslots` → `Number of free actor slots in the room (deprecated, always returns 0)`
- `freemissionactorslot` → `true iff there is a free mission actor slot in the room`
- `slotcontext` → `The component which contains entity slots related to this room. For virtual rooms, it will be the controllable otherwise the room itself`
- `ischairslot.{$componentslot}` → `true if $componentslot is a NPC position slot within this room and related to a chair`
- `chairapproachslot.{$componentslot}` → `The approach slot of a NPC position slot related to a chair in this room`
- `chairbaseslot.{$componentslot}` → `The base chair slot of a NPC position slot related to a chair in this room. Used as a static anchor slot for the chair and can be used as a NPC waypoint.`
- `chairroomslot.{$componentslot}` → `The room slot related to a chair in this room, to be used by NPCs for destination reservation.`
- `controlposition.{$controlposition}.exists` → `true if the specified control position exists`
- `controlposition.{$controlposition}.roomslot` → `Slot which entities inhabit when working at the specified control position`
- `controlposition.{$controlposition}.entity` → `Entity currently working at the specified control position`
- `controlpositions.list` → `List of component slots which are control positions`
- `hascontrolpanel.{$controlpaneltype}` → `true if this room has a control panel of the specified type`

## `dockingbay` — inherits `room` (28 direct properties)

- `assignedship` → `The ship currently assigned to this dock`
- `pier` → `The pier module containing this dock`
- `maxoffset.{$sizetag}.position` → `Position range away from the launchpos in which a ship must be to land`
- `maxoffset.{$sizetag}.rotation` → `Rotation range away from the launchpos in which a ship must be to land`
- `maxoffset.{$ship}.position` → `Position range away from the launchpos in which a ship must be to land, taking installed docking software into account`
- `maxoffset.{$ship}.rotation` → `Rotation range away from the launchpos in which a ship must be to land, taking installed docking software into account`
- `docksize` → `Tag list of supported dock sizes`
- `docked` → `List of docked ships`
- `external` → `true iff this is an external dockingbay (= ship visible while docked)`
- `shipstorage.capacity` → `Number of ships in total that can fit in this docking bay`
- `shipstorage.free` → `Number of ships that can currently fit in this docking bay`
- `isstorage` → `true if this is an internal storage bay`
- `isdockingallowed` → `true if this is not exclusively for undocking`
- `isunitdockingallowed` → `true if units may dock here, even if other ships may not`
- `isundockingallowed` → `true if this is not exclusively for docking`
- `isunitundockingallowed` → `true if units may undock from here, even if other ships may not`
- `dockslot` → `Slot on docking bay to which ship connects when docked`
- `todockpos` → `Position on docking bay to which ship flys in order to dock`
- `launchpos` → `Position on docking bay from which ship can safely return to normal flight`
- `dockstate` → `The dock's current state`
- `isbuildingallowed` → `true if building is allowed at this dock`
- `istradingallowed` → `true if trading is allowed at this dock`
- `isplayeronly` → `true if this dock is exclusively used for the player`
- `isshowroom` → `true if this dock is exclusively used as a showroom`
- `isventureronly` → `true if this dock is exclusively used for venturers`
- `ventureplatform` → `The venture platform with which this docking bay is associated`
- `islaunchtube` → `true if this dock is considered a launchtube (external and either docking not allowed or has forced undockingspeed)`
- `ishidden` → `true if this dock and its content is flagged to be hidden in the UI`

## `walkablemodule` — inherits `module` (4 direct properties)

- `hasentrypos` → `true iff position for dock area entry is defined`
- `entrypos` → `Dock area entry position`
- `hasexitpos` → `true iff position for dock area exit is defined`
- `exitpos` → `Dock area exit position`

## `dockarea` — inherits `walkablemodule` (4 direct properties)

- `isventuremodule` → `true if this module is for use with venture platforms`
- `ventureplatform` → `The venture platform with which this docking bay is associated`
- `dock.{$docksize}` → `Suitable dock for this docksize available to this dockarea (can be occupied)`
- `freedock.{$docksize}` → `Suitable free dock for this docksize available to this dockarea`

## `space` — inherits `component` (17 direct properties)

- `economy` → `Economy value for this space`
- `security` → `Security value for this space`
- `sunlight` → `Sunlight value for this space`
- `god` → `God entries allowed for this space`
- `jobs` → `Job entries allowed for this space`
- `isexclusiveforextensionjobs` → `Is the space exclusive for job definitions of its own extension, affecting potential spawn location and jobmainsector/zone selection. Inherits exclusivity from parent spaces.`
- `factionlogic` → `Faction logic allowed for this space`
- `locationtags` → `List of tags relevant to this space location`
- `alllocationtags` → `List of tags relevant to this space location and all parent spaces`
- `hasownlocationtag.{$tag}` → `Does the specified tag exist in the list of tags defined for this space?`
- `hasownlocationtag.<tagname>` → `Shortcut for hasownlocationtag.{tag.<tagname>}`
- `haslocationtag.{$tag}` → `Does the specified tag exist in the list of tags defined for this space or any parent spaces?`
- `haslocationtag.<tagname>` → `Shortcut for haslocationtag.{tag.<tagname>}`
- `accesslicence` → `Licence type required for access to this space (null if no restriction)`
- `accessrestricted` → `Access to this space restricted (for player assets)`
- `freejobquota.{$jobid}` → `Available quota for ships of the specified job to be assigned to this space (not checking suitability of space; see $space.issuitableforjob)`
- `issuitableforjob.{$jobid}` → `Does this space match the location criteria for the specified job?`

## `galaxy` — inherits `space` (1 direct properties)

- `representatives` → `List of all faction representatives in the galaxy`

## `cluster` — inherits `space` (29 direct properties)

- `isnormalcluster` → `true iff normal cluster (not presentation cluster, not venturer cluster, not exploration cluster)`
- `ispresentation` → `true iff cluster is used for presentation scenes e.g. cutscenes`
- `isexploration` → `true iff cluster is used for exploration`
- `isventurer` → `true iff cluster is used for ships on ventures`
- `systemid` → `the system ID of the cluster, used to identify which star system the cluster belongs to. This property is 0 if the cluster is the only cluster in the system`
- `gravidarfactorat.{$position}` → `Gravidar factor at the given cluster position`
- `hashazardousregionat.{$position}` → `Whether the given cluster position is inside a hazardous region`
- `isregioncurrentlyhazardousat.{$position}` → `Whether the given cluster position is inside a region that is currently hazardous`
- `planets` → `List of part names related to planets (data defined in mapdefaults.xml)`
- `moons.{$string}` → `List of part names related to moons of the specified planet (data defined in mapdefaults.xml)`
- `world.{$string}.size` → `Diameter of the of the world of specified part name`
- `world.{$string}.position.{$component}` → `Position of the world of specified part name, relative to $component`
- `terraforming.partname` → `The template part name of the planet that can be terraformed`
- `terraforming.planetposition.{$component}` → `The position of the planet that can be terraformed, relative to $component`
- `terraforming.stat.{$statid}.exists` → `true iff the terraforming stat is either dynamic or has been set manually`
- `terraforming.stat.{$statid}.value` → `The raw value of the terraforming stat`
- `terraforming.stat.{$statid}.state` → `The state number of the terraforming stat (corresponds to a color in the UI)`
- `terraforming.activeproject.exists` → `true if there is an active terraforming project`
- `terraforming.activeproject.isaborted` → `true if the active terraforming project has been aborted`
- `terraforming.activeproject.id` → `The ID of the active terraforming project. Null if there is no current project.`
- `terraforming.project.{$projectid}.exists` → `Whether the terraforming project exists on this planet`
- `terraforming.project.{$projectid}.name` → `The name of the terraforming project`
- `terraforming.project.{$projectid}.description` → `The description of the terraforming project`
- `terraforming.project.{$projectid}.complete` → `Whether the terraforming project has been completed at least once`
- `terraforming.project.{$projectid}.successchance` → `The terraforming project's chance of success upon completion`
- `terraforming.project.{$projectid}.resources` → `Total Required scaled-resources for this project to complete`
- `terraforming.mission.active` → `Whether the terraforming mission for this cluster has been accepted`
- `terraforming.mission.complete` → `Whether the terraforming mission for this cluster has been completed`
- `terraforming.habitable` → `true if the terraforming world is habitable`

## `sector` — inherits `space` (18 direct properties)

- `averagedistancetolockbox` → `Average distance to a lockbox from any point in this sector. (-1m if not possible to get a lockbox in this sector)`
- `iscontested` → `true iff there are two or more factions currently vying for ownership of the sector`
- `iscontestedby.{$faction}` → `true iff sector is contested by specified faction`
- `contestingfactions` → `List of factions contesting this sector`
- `hasgravidarobscuringregion` → `true if the sector has a gravidar obscuring region.`
- `gravidarfactorat.{$position}` → `Gravidar factor at the given sector position`
- `hashazardousregion` → `true if the sector has a hazardous region.`
- `hashazardousregionat.{$position}` → `Whether the given sector position is inside a hazardous region`
- `isregioncurrentlyhazardousat.{$position}` → `Whether the given sector position is inside a region that is currently hazardous`
- `resources` → `All region resource wares`
- `yieldrating.{$ware}` → `The sector's current yield rating for this ware (0 to 15)`
- `bestyieldrating.{$ware}` → `The sector's best yield rating for this ware (0 to 15)`
- `containsthewave` → `true if the sector is flagged to contain The Wave anomaly`
- `waveprotectionresources` → `Wares required for an object to be protected from The Ware anomaly. 1 unit of each ware is required for protection.`
- `policefaction` → `Police faction for this sector, which is the police faction of the sector owner (may be null)`
- `typicallockboxmacro` → `Macro of a lockbox typically found in this sector`
- `coreposition` → `The center position of the area considered the core of the sector, in sector coordinates`
- `coresize` → `The diameter of the area considered the core of the sector`

## `zone` — inherits `space` (11 direct properties)

- `adjacentzones` → `List of adjacent zones`
- `haspriority` → `true iff zone has highest priority in its area. false for highways`
- `policefaction` → `Police faction for this zone, which is the police faction of the zone owner (may be null)`
- `istempzone` → `true iff the zone is currently a temporary zone`
- `isnormalzone` → `true iff the zone is currently a normal zone (not temporary, not gate zone and not highway)`
- `isalwaysnormalzone` → `true iff the zone is always a normal zone (not temporary, not gate zone and not highway)`
- `size` → `Zone size (edge length)`
- `hashazardousregionat.{$position}` → `Whether the given zone position is inside a hazardous region`
- `isregioncurrentlyhazardousat.{$position}` → `Whether the given zone position is inside a region that is currently hazardous`
- `islocalhighway` → `true iff zone is a local highway`
- `issuperhighway` → `true iff zone is a superhighway`

## `highway` — inherits `zone` (9 direct properties)

- `isdisabled` → `true iff highway is disabled (currently only possible through custom gamestart)`
- `origin` → `Highway origin zone`
- `destination` → `Highway destination zone`
- `junctions` → `List of zones along a highway`
- `entry` → `Highway entry gate`
- `exit` → `Highway exit gate`
- `entryjumpgate` → `Jumpgate which leads into this highway`
- `exitjumpgate` → `Jumpgate which this highway leads into`
- `closestpointtoplayer` → `Closest highway point to player in highway coordinates (x=y=0, z-coord range 0-1)`

## `region` — inherits `component` (0 direct properties)


## `entity` — inherits `component` (66 direct properties)

- `customhandler` → `true iff the entity has a custom conversation handler`
- `type` → `Entity type`
- `typename` → `Entity type name`
- `controlpost` → `Entity's current control post`
- `role` → `Entity's current role`
- `roleobject` → `Object this entity is assigned to for their role`
- `titleoverride` → `Entity's title override`
- `iconoverride` → `Entity's icon override`
- `occupationname` → `Entity's occupation name`
- `icon` → `Entity's icon ID`
- `race` → `The entity's race`
- `page` → `Voice text page ID`
- `isfemale` → `Is entity female`
- `isavatar` → `Is entity an avatar of another`
- `iscommable` → `Can communication be initiated with this entity`
- `ismissionactor` → `Is a mission actor`
- `isremotecommable` → `Is remote commable (only relevant for NPC actors, not NPC templates and is automatically set when NPC is instanced and unset when creating a template)`
- `iscontrolentity` → `Is a control entity`
- `isintransit` → `Is the entity in transit to a location?`
- `isbusy` → `Is the entity flagged as busy?`
- `istransferscheduled` → `Is a crew transfer order scheduled for the entity?`
- `istemporary` → `Is the entity temporary?`
- `ishidden` → `Is the entity hidden?`
- `podarrivaltime` → `Scheduled time of arrival at current object in a crew transfer pod, or null if not being transferred via pod`
- `roomslot` → `The slot assigned for this entity. The entity may not be at this offset but in-transit to it. (component may be a room or object)`
- `floortags` → `A list of floor tags of the entities current floor`
- `iswalking` → `Is the NPC currently walking`
- `slowwalkspeed` → `Defined slow walk speed of this entity`
- `walkspeed` → `Defined walk speed of this entity`
- `runspeed` → `Defined run speed of this entity`
- `isspeaking` → `Is the entity currently speaking?`
- `isinspeakrange` → `Is the entity close enough to the player to speak directly without using comms?`
- `isinspeakrange.{$entity}` → `Is the entity close enough to the supplied recipient entity to speak directly without using comms?`
- `lastspeaktime` → `Time of when the entity was last speaking, or null if entity has never spoken (at least not since lastspeaktime support was added in X4 v6.00)`
- `experienceprogress` → `Boarding experience progress`
- `neededexperience` → `Needed boarding experience for next level`
- `skill.{$skilltype}` → `Skill value between 0 and 15 of the supplied skill type`
- `skill.<skillname>` → `Shortcut for skill.{skilltype.<skillname>}`
- `combinedskill` → `Combined skill value between 0 and 100, based on weighted skills that are relevant for the entity's control post`
- `potentialskill.{$entityrole}` → `Potential combined skill value between 0 and 100, based on weighted skills that are relevant for the role`
- `potentialskill.{$controlpost}` → `Potential combined skill value between 0 and 100, based on weighted skills that are relevant for the control post`
- `controlled` → `Object controlled by the entity`
- `assignedcontrolled` → `Object assigned to be controlled by the entity`
- `spacesuit` → `The spacesuit the entity is in, or null`
- `spacesuitmacro` → `The macro the entity is defined to use`
- `dockarea` → `The dock area this entity is currently on`
- `buildmodule` → `The build module this entity is currently on`
- `walkablemodule` → `The walkable module (dock area or build module) this entity is currently on`
- `inventory` → `Wares currently in entity's inventory`
- `stock` → `Wares in entity's stock list`
- `cancraft.{$ware}` → `Can craft inventory ware`
- `command.value` → `Script command that the entity is executing`
- `command.param` → `Primary parameter of the current script command`
- `command.param2` → `Secondary parameter of the current script command`
- `commandaction.value` → `Script command action that the entity is executing`
- `commandaction.param` → `Primary parameter of the current script command action`
- `$<variable>` → `Value of variable on entity's blackboard`
- `shouldinformplayer` → `true iff entity is on a player-owned ship that either has the player.occupiedship or a ship without a pilot as commander and that has no looped orders`
- `shouldwarnplayer` → `true iff entity is on a player-owned ship that either has the player.occupiedship or a ship without a pilot as commander or has no commander at all and that has no looped orders`
- `istradecomputer` → `Is this entity assigned as a trade computer to process trade operations on the player-controlled ship?`
- `isshadyguy` → `Is this entity assigned as a black marketeer to handle extralegal business?`
- `isrepresentative` → `Is this entity a faction representative?`
- `isdiplomat` → `Is this entity a faction diplomat?`
- `isindependent` → `whether ownership of this entity is independent of ownership of object to which they are assigned (always true if entity has no control post or role)`
- `tradesvisible` → `true iff the entity's trades are visible to the player`
- `facecutscene` → `Face cutscene key for this entity, or null if no default is defined`

## `nonplayer` — inherits `entity` (0 direct properties)


## `npc` — inherits `nonplayer` (9 direct properties)

- `npctemplate` → `The template for this NPC which can be used to check against the list of people on an object`
- `targetslot` → `The slot currently set as the next target for a moving NPC. The NPC may not be at this offset but in-transit to it. (component may be a room or object)`
- `currentchair` → `The chair slot the NPC is currently inhabiting. Not set when moving towards the chair. (component may be a room or object)`
- `hasclothingmod` → `Whether the NPC has any clothing mod installed`
- `hasclothingmod.{$ware}` → `Whether the NPC has a clothing mod based on the specified clothing mod ware installed`
- `hastool` → `Whether the NPC currently carries a tool`
- `hasbody` → `Whether the NPC currently has a body capable of performing animations`
- `isinconversation` → `Is the NPC currently involved in a player conversation?`
- `diplomacy.ship` → `The ship assigned to assist the NPC in diplomacy actions`

## `weapon` — inherits `destructible` (17 direct properties)

- `ammo.capacity` → `Amount of ammostorage this weapon adds to its destructible`
- `ammo.macro` → `Macro of the used ammo`
- `ammo.ware` → `Ware that can provide the used ammomacro`
- `ammo.iscompatible.{$macro}` → `true iff the supplied ammo macro (missile) is compatible with this weapon`
- `isinactiveweapongroup` → `Is installed on a defensible and is in an active weapon group`
- `isreadytofire` → `Is ready to fire (weapon active, turret deployed)`
- `mode` → `Mode this weapon/turret is operating in`
- `isrepairing` → `Whether the weapon is for repairing`
- `ismining` → `Whether the weapon is for mining`
- `iscombat` → `Whether the weapon is neither for repairing nor for mining`
- `barrelposition` → `The position of the weapon's barrel (may be 0,0,0 for weapons with no collision)`
- `maxfirerange` → `Maximum firing range`
- `isbeam` → `Whether the weapon fires a beam`
- `isguided` → `Whether the weapon fires guided missiles`
- `istorpedo` → `Whether the weapon fires torpedoes`
- `reloadrate` → `Number of times this weapon fires its default bullet in one second`
- `reloadtime` → `Amount of time between bullet discharges when firing its default bullet`

## `turret` — inherits `weapon` (0 direct properties)


## `missileturret` — inherits `turret` (0 direct properties)


## `detector` — inherits `object` (1 direct properties)

- `isdetecting.{$component}` → `true iff the other component is currently being detected by this one`

## `componentslot` (19 direct properties)

- `component` → `The component part of the componentslot`
- `name` → `Slot connection name`
- `tags` → `List of tags defined on the connection`
- `hastag.{$tag}` → `Does the specified tag exist in the list of tags defined on the connection?`
- `hastag.<tagname>` → `Shortcut for hastag.{tag.<tagname>}`
- `hasanytag.{$list}` → `true iff the connection contains any tag from the list`
- `hasalltags.{$list}` → `true iff the connection contains all tags from the list`
- `floortags` → `List of walking relevant tags for the floor at this component slot (requires the component to have physics)`
- `group` → `The group defined on the connection`
- `offset` → `The offset position of the connection (relative to the slot's component)`
- `relativeposition.{$component}` → `The offset position of the connection relative to $component`
- `rotation` → `The rotation of the connection (relative to the slot's component)`
- `relativerotation.{$component}` → `The rotation of the connection relative to $component`
- `staticoffset` → `The static offset position of the connection (ignoring offset changes due to animation)`
- `staticrotation` → `The static rotation of the connection (ignoring offset changes due to animation)`
- `controlposition` → `Control position type if this slot is a control position for an entity, otherwise null`
- `distanceto.{$component}` → `Distance from this componentslot's offset to $component`
- `distanceto.{$componentslot}` → `Distance from this componentslot's offset to the component and connection offset of $componentslot`
- `distanceto.[$component, $position]` → `Distance from this componentslot's offset to the $position relative to $component`

## `macroslot` (9 direct properties)

- `macro` → `The macro part of the macroslot`
- `name` → `Slot connection name`
- `tags` → `List of tags defined on the connection`
- `hastag.{$tag}` → `Does the specified tag exist in the list of tags defined on the connection?`
- `hastag.<tagname>` → `Shortcut for hastag.{tag.<tagname>}`
- `offset` → `The offset position of the connection relative to its parent connect`
- `rotation` → `The rotation of the connection relative to its parent connect`
- `staticoffset` → `The static offset position of the connection relative to the macro (taking into account parent connection offsets)`
- `staticrotation` → `The static rotation of the connection relative to the macro (taking into account parent connection offsets)`

## `trade` (49 direct properties)

- `exists` → `true iff trade exists`
- `available` → `true iff trade exists and is available`
- `buyer` → `The buyer container if defined`
- `seller` → `The seller container if defined`
- `owner` → `Owner container (seller or buyer)`
- `isbuyoffer` → `true iff trade is a buy offer`
- `isselloffer` → `true iff trade is a sell offer`
- `isoffer` → `true iff trade is an offer`
- `isorder` → `true iff trade is an order (deal)`
- `ware` → `Trade ware`
- `ispricelocked.{$container}` → `true iff the price of the trade ware is locked on the trade partner of the given container`
- `amount` → `Trade amount`
- `desiredamount` → `Trade desired amount (really wanted amount, which may exceed affordable amount)`
- `offeramount` → `Trade amount plus all the reserved amounts`
- `offeramount.{$object}` → `Trade amount plus the reserved amount for this object`
- `minamount` → `Minimum trade amount`
- `transferredamount` → `Amount of wares that has been transferred for this trade`
- `destroyedamount` → `Amount of wares that has been destroyed for this trade`
- `volume` → `Total volume of trade amount`
- `offervolume` → `Trade volume plus all the reserved volumes`
- `offervolume.{$object}` → `Trade volume plus the reserved volume for this object`
- `minvolume` → `Total volume of minimum trade amount`
- `price` → `Total price of trade amount`
- `unitprice` → `Price for a single unit`
- `minprice` → `Total price of minimum trade amount`
- `relativeprice` → `Current price between min and max as a value from -1.0 to +1.0`
- `quantityfactor` → `Current price/average price ratio`
- `hasdynamicprice` → `true if the trade does not have a fixed price (such as when the player sets a price at a player-owned station)`
- `stocklevel` → `Ratio trade amount / target amount ratio (target amount of seller or buyer - for selloffers/buyoffers respectively. (see container.cargo.{$ware}.target)`
- `stocklevel.{$amount}` → `Ratio amount / target amount ratio (target amount of seller or buyer - for selloffers/buyoffers respectively. (see container.cargo.{$ware}.target)`
- `bundle` → `true iff the trade is flagged for converting ammo/units into wares on transfer`
- `unbundle` → `true iff the trade is flagged for converting a ware into ammo/units on transfer`
- `ismission` → `true iff the trade was spawned using a mission cue`
- `missioncue` → `mission cue used to spawn object`
- `tradeoffer` → `source trade offer (for trade orders derived from a specific offer)`
- `buyfree` → `true iff the trade is flagged so that the buyer does not actually spend any money (seller would still receive money, unless $trade.sellfree is also true)`
- `buyfree.{$object}` → `true iff the trade will be free for this particular buyer-object (seller would still receive money, unless $trade.sellfree is also true)`
- `sellfree` → `true iff the trade is flagged so that the seller does not actually receive any money (buyer would still have to spend money, unless $trade.buyfree is also true)`
- `sellfree.{$object}` → `true iff this particular seller-object would not actually receive any money (buyer would still have to spend money, unless $trade.buyfree is also true)`
- `iswareexchange` → `true iff the trade is used to facilitate ware exchange or crew exchange`
- `isshiptoship` → `true iff both trade partners are ships with corresponding active/passive trade orders (only supported for ware/crew exchange trades)`
- `iscrewexchange` → `true iff the trade is used to facilitate ship-to-ship crew exchange`
- `isbuyerpassive` → `true iff the buyer of this ship-to-ship ware/crew exchange is flagged as being the passive party (stationary)`
- `issellerpassive` → `true iff the seller of this ship-to-ship ware/crew exchange is flagged as being the passive party (stationary)`
- `ispassive.{$container}` → `true iff the trade is used for ship-to-ship ware/crew exchange and the supplied container is the passive party (stationary)`
- `exchangepartner.{$container}` → `The exchange partner for this trade deal. Used for trade orders to specify who is trading with whom when the trade deal only has buyer OR seller defined. Will return the 'other' container if $container is part of the trade.`
- `restriction.factions` → `List of factions that are allowed to perform the trade (empty if unrestricted, modified by restriction.inverted)`
- `restriction.inverted` → `true iff the faction restriction is inverted and the trade is available to everyone except the restriction.factions`
- `cantradewith.{$container}` → `true iff the supplied container is allowed to be involved with this trade`

## `build` (30 direct properties)

- `exists` → `true iff build order exists`
- `iscancelled` → `true if build order has been cancelled`
- `isshipbuild` → `true if build task is to build a ship`
- `isrecycleshipbuild` → `true if build task is to recycle a ship`
- `isexpansion` → `true if build task is to expand an existing station`
- `isupgrade` → `true if build task is to upgrade an existing ship`
- `issoftwareonlyupgrade` → `true if build task is to exclusivly upgrade software on an existing ship`
- `isrestock` → `true if build task is to restock an existing ship`
- `isshipmodification` → `true if build task is either to restock or upgrade an existing ship`
- `isprocessing` → `true if the build task is currently being processed`
- `mayrequireconstructionvessel` → `true if build task may require a construction vessel at some stage, based on the type of build and the module set`
- `object` → `The object assigned to build this task`
- `buildmodule` → `The build module assigned to build this task`
- `buildprocessor` → `The build processor assigned to build this task`
- `buildobject` → `The object being built. either 'base' or 'construction', whichever is valid`
- `base` → `Pre-existing object to be built via this build order (can not be valid alongside 'construction')`
- `construction` → `Newly created object, constructed by this build order (can not be valid alongside 'base')`
- `macro` → `Macro to be built`
- `faction` → `Faction of the built object`
- `time` → `The gametime when this build task was created`
- `age` → `How long ago this build task was created`
- `loadout` → `Loadout ID of the build order. null if custom or omitted`
- `loadoutfaction` → `Faction specified for the loadout of the built object if that can be retrieved from the spawnsource. Falls back to faction of the built object`
- `constructionsequence` → `Construction sequence for the build (or null if none exists)`
- `consumables` → `Table of consumable amounts. macro is the key of the table`
- `price` → `Set price of the build order when it was added`
- `transferredamount` → `The amount of money already transferred, negative being refunded to the player, positive being paid by the player`
- `zone` → `Space in which the build will take place`
- `position` → `Position of the build in 'zone'`
- `rotation` → `Rotation of the build in 'zone'`

## `operation` (4 direct properties)

- `exists` → `true iff the operation exists`
- `starttime` → `The gametime when the operation was started`
- `duration` → `The expected duration of the operation until its conclusion. -1s if no duration is specified.`
- `owner` → `Faction defined as the owner of this operation`

## `boardingoperation` — inherits `operation` (22 direct properties)

- `boardee` → `Target of a boarding operation`
- `attackers` → `Attackers of a boarding operation`
- `approachingpods` → `Boarding pods approaching the target`
- `allmarinesdispatched` → `Have all marines set to join this this boarding operation been dispatched? (true if no marines have been assigned from any attacker)`
- `marines.infiltrating.list` → `List of infiltrating marines taking part in the operation as NPC templates`
- `marines.infiltrating.count` → `Number of infiltrating marines taking part in the operation`
- `marines.infiltrating.combinedskill` → `Combined skill value (between 0 and 100 per individual) of all infiltrating marines`
- `marines.infiltrating.{$npctemplate}` → `NPC template entry of a infiltrating marine matching the provided npctemplate (raw npctemplates can not provide information without the operation as context - see npctemplateentry)`
- `marines.infiltrating.random` → `A random NPC template entry of an infiltrating marine`
- `marines.fighting.list` → `List of fighting marines taking part in the operation as NPC templates`
- `marines.fighting.count` → `Number of fighting marines taking part in the operation`
- `marines.fighting.combinedskill` → `Combined skill value (between 0 and 100 per individual) of all fighting marines`
- `marines.fighting.{$npctemplate}` → `NPC template entry of a fighting marine matching the provided npctemplate (raw npctemplates can not provide information without the operation as context - see npctemplateentry)`
- `marines.fighting.random` → `A random NPC template entry of a fighting marine`
- `marines.killed.list` → `List of killed marines which were taking part in the operation as NPC templates`
- `marines.killed.count` → `Number of killed marines which were taking part in the operation`
- `marines.killed.combinedskill` → `Combined skill value (between 0 and 100 per individual) of all killed marines`
- `marines.killed.{$npctemplate}` → `NPC template entry of a killed marine matching the provided npctemplate (raw npctemplates can not provide information without the operation as context - see npctemplateentry)`
- `marines.killed.random` → `A random NPC template entry of a killed marine`
- `boardingphase` → `Current phase of the boarding operation`
- `boardingapproachthreshold` → `Threshold value of the boarding operation in regards to having the boarding pods launch and approach the target`
- `boardinginsertionthreshold` → `Threshold value of the boarding operation in regards to attempting to insert marines into the target`

## `diplomacyactionoperation` — inherits `operation` (10 direct properties)

- `agent` → `The agent entity assigned to this operation`
- `agentresult` → `The resulting state of the agent at the operation's conclusion`
- `action.id` → `The id of this operation's diplomacy action`
- `action.name` → `The name of the diplomacy action`
- `action.description` → `The description of the diplomacy action`
- `action.shortdescription` → `The short description of the diplomacy action`
- `action.duration` → `The base duration of the diplomacy action`
- `action.gift` → `The chosen ware to be presented as a gift to the target faction`
- `action.agent.experience` → `The base recommended minimum agent experience of the diplomacy action`
- `action.$<param>` → `Value of diplomacy action parameter`

## `diplomacyeventoperation` — inherits `operation` (14 direct properties)

- `faction` → `The first involved faction in a diplomacy event`
- `otherfaction` → `The second involved faction in a diplomacy event`
- `source` → `Diplomacy action operation which resulted in this event operation (may be null)`
- `agent` → `The agent entity assigned to this operation`
- `agentresult` → `The resulting state of the agent at the operation's conclusion`
- `event.id` → `The id of this operation's diplomacy event`
- `event.source` → `The diplomacy action id which was the source of this diplomacy event operation, or null if none is defined.`
- `event.name` → `The name of the diplomacy event`
- `event.description` → `The description of the diplomacy event`
- `event.shortdescription` → `The short description of the diplomacy event`
- `event.conclusiontext` → `The base conclusion text for the diplomacy event`
- `event.duration` → `The base duration of the diplomacy event`
- `option` → `The data for currently selected option`
- `outcome` → `The data for the ultimate outcome`

## `diplomacyeventoperationoption` (10 direct properties)

- `exists` → `true iff the event option exists`
- `id` → `The ID of the event option`
- `resulttext` → `The text describing the result if this option is performed`
- `conclusiontext` → `The text to presented at the conclusion of this option`
- `weight` → `The base weight for this option to be chosen as the outcome which may be modified when selected by the player and an agent assigned`
- `relation` → `The result relation between the two factions if this option is chosen as the outcome`
- `agent.risk` → `The risk to an agent when assigned to this option`
- `cost.influence` → `The influence cost to be paid at conclusion of this event if this option is selected`
- `cost.money` → `The money cost to be paid at the conclusion of this event if this option is selected`
- `cost.wares` → `The inventory wares to be removed from the player at the conclusion of this event if this option is selected`

## `licence` (10 direct properties)

- `exists` → `true iff licence exists`
- `name` → `Licence name`
- `rawname` → `Raw licence name, as text entry reference`
- `description` → `Licence description`
- `minrelation` → `Min relation to acquire this licence`
- `precursor` → `Licence type to acquire this licence`
- `price` → `Licence price`
- `issellable` → `true iff licence is sellable from traders`
- `faction` → `Faction`
- `type` → `Licence type`

## `group` (5 direct properties)

- `count` → `Number of components in the group`
- `list` → `List of all components in the group`
- `{$numeric}` → `The $numeric-th component in the group (1-based)`
- `random` → `A random component from the group (the group must be non-empty)`
- `indexof.{$component}` → `Index of $component in the group (1-based), or 0 if not present`

## `order` (22 direct properties)

- `exists` → `true iff order exists`
- `id` → `ID`
- `name` → `Name`
- `rawname` → `Raw name, as text entry reference`
- `script` → `Name of the AI script associated with the order`
- `description` → `Description`
- `object` → `The object to which this order is given`
- `state` → `State`
- `canplayercancel` → `true iff order can be cancelled by the player (order is either in a non-critical state or supports being cancelled by specific player actions while in the critical state)`
- `isinfinite` → `true iff order is infinite`
- `isinloop` → `true iff order is in an order loop`
- `istemporary` → `true iff order is temporary (i.e. it will be removed when complete, even when in an order loop)`
- `haspriority` → `true iff order is a priority order (i.e. it was enqueued before other orders)`
- `isoverride` → `true iff order is an override order`
- `isrunning` → `true iff order is currently running (state is either started, critical or finish)`
- `isparameditable.<param>` → `true iff order parameter is currently editable (see <edit_order_param> for more information)`
- `istradecomputer` → `true iff order is a trade computer order (to be processed by a trade computer on player-controlled ship)`
- `trade` → `Trade that is associated with this order, or null`
- `build` → `Build task that is associated with this order, or null`
- `operation` → `Operation that is associated with this order, or null`
- `requiredskill` → `Required combined skill of control entity to execute order`
- `$<param>` → `Value of order parameter`

## `constructionsequence` (11 direct properties)

- `count` → `Number of entries in construction sequence`
- `{$numeric}` → `The $numeric-th construction plan entry in this sequence`
- `{$constructionplanentryid}` → `The matching construction plan entry in this sequence`
- `isfixed` → `true iff the sequence is flagged as fixed and cannot be adjusted`
- `hasstages` → `true iff the sequence has stages defined`
- `finalsequence` → `A copy of the full staged sequence (null if the sequence does not have stages)`
- `stage.count` → `The number of stages defined for this sequence`
- `stage.current` → `The stage the sequence is currently set to construct to (only applicable for sequences to be used for build tasks)`
- `stage.{$numeric}.first` → `The index of the first module in the specified stage`
- `stage.{$numeric}.last` → `The index of the last module in the specified stage`
- `stage.{$numeric}.sequence` → `A copy of the whole sequence including stages but with the current stage set to the specified stage`

## `constructionplanentryid` (0 direct properties)


## `constructionplanentrydata` (5 direct properties)

- `exists` → `true iff the construction plan entry exists in the construction sequence`
- `id` → `The construction plan entry`
- `macro` → `The macro of the construction plan entry`
- `loadout` → `The upgrade loadout of the construction plan entry`
- `stage` → `The stage number of this plan entry`

## `loadout` (1 direct properties)

- `wares` → `All equipment wares in the loadout`

## `fleetunit` (7 direct properties)

- `exists` → `true iff fleet unit exists`
- `object` → `Existing controllable for this fleet unit, set after a build task has been processed`
- `toplevelcommander` → `Top-level commander object and leader of the fleet`
- `owner` → `Owner faction of the fleet`
- `macro` → `Controllable-class macro of the fleet unit to be reconstructed`
- `loadout` → `Loadout of the fleet unit to be reconstructed`
- `build` → `Build task constructing the replacement object of this fleet unit`

## `list` (11 direct properties)

- `count` → `Number of elements in the list`
- `clone` → `A shallow copy of the list`
- `{$numeric}` → `The $numeric-th element in the list (1-based)`
- `last` → `The last element in the list (the list must be non-empty)`
- `random` → `A random element from the list (the list must be non-empty)`
- `randominrange` → `A random value in the range between the lowest and highest value in the list, of the matching numeric datatype; intended usage is [$min, $max].randominrange (the list must be non-empty and all elements must be numeric)`
- `indexof.{$value}` → `Index of first occurrence of $value in the list (1-based), or 0 if not found`
- `countof.{$value}` → `Number of elements equal to $value in the list`
- `min` → `The minimum value in the list (all elements must be numeric), or null if the list is empty`
- `max` → `The maximum value in the list (all elements must be numeric), or null if the list is empty`
- `average` → `The average of all list elements (all elements must be numeric), or null if the list is empty`

## `table` (9 direct properties)

- `clone` → `A shallow copy of the table`
- `keys.count` → `Number of keys in the table`
- `keys.list` → `List of all keys in the table (reliably sorted if all keys are numeric, otherwise order can change between savegames)`
- `keys.sorted` → `List of all keys in the table, sorted by their associated values (requires all values to be numeric)`
- `keys.random` → `A random key in the table (the table must be non-empty)`
- `keys.{$numeric}` → `The $numeric-th key in the table (1-based), note that this lookup can be inefficient and order can change between savegames`
- `keys.last` → `The last key in the table (reliable if all keys are numeric, otherwise order can change between savegames; the table must be non-empty)`
- `{$key}` → `Value associated with the table key (type is ignored for numeric keys, e.g. 50s and 50m are treated as the same key)`
- `$<keyname>` → `Value associated with the table key (shortcut for {'$<keyname>'}, all string keys must begin with '$')`

## `string` (1 direct properties)

- `[$arg1, $arg2, ...]` → `Creates a new string by replacing %1, %2, ... in the string with corresponding list elements`

## `position` (6 direct properties)

- `x` → `X coordinate`
- `y` → `Y coordinate`
- `z` → `Z coordinate`
- `length` → `Estimated distance of the position from the centre of the reference space (interpreting the position as vector from the point of origin)`
- `distanceto.{$position}` → `Distance to the provided position (assuming they are in the same space)`
- `rotation` → `Rotation value as seen from the centre of the reference space (interpreting the position as vector from the point of origin)`

## `vector` (6 direct properties)

- `x` → `X coordinate`
- `y` → `Y coordinate`
- `z` → `Z coordinate`
- `length` → `Estimated length of the vector`
- `distanceto.{$vector}` → `Distance to the provided vector`
- `rotation` → `Rotation value with this vector as its forward direction`

## `rotation` (7 direct properties)

- `yaw` → `Yaw angle`
- `pitch` → `Pitch angle`
- `roll` → `Roll angle`
- `inverse` → `Inverse rotation`
- `forward` → `The forward direction vector`
- `right` → `The right direction vector`
- `up` → `The up direction vector`

## `faction` — inherits `dbdata` (59 direct properties)

- `id` → `ID`
- `name` → `Name`
- `rawname` → `Raw name, as text entry reference`
- `knownname` → `Name, ignoring the unknown-status`
- `shortname` → `Short name`
- `prefixname` → `Prefix name`
- `spacename` → `Space name`
- `homespacename` → `Home space name`
- `description` → `Description`
- `hasbeenrenamed` → `true iff the faction has been renamed`
- `primaryrace` → `Primary race of faction`
- `isactive` → `true if the faction is currently active`
- `knowntoplayer` → `true if the faction is known to the player`
- `policefaction` → `Police faction for this faction (possibly the same faction, can also be null)`
- `defaultpolicefaction` → `Default police faction for this faction (possibly the same faction, can also be null)`
- `teamname` → `Online team name of this faction (custom name or localised default team name)`
- `customteamname` → `Custom online team name of this faction, or empty string if no custom name is set`
- `relation.<relationrange>.min` → `relation value at the lower bound of the specified range (lowest value in the range, except for ranges 'neutral' and 'dock', in which this value is NOT included)`
- `relation.<relationrange>.mid` → `middle relation value in the specified range`
- `relation.<relationrange>.max` → `relation value at the upper bound of the specified range (highest value in the range, except for range 'neutral', in which this value is NOT included)`
- `relation.{$numeric}.uivalue` → `UI representation value (-30 to +30) of the specified relation value for this faction`
- `hasrelation.<relationrange>.{$component}` → `true iff the relation to owner of $component is in specified range`
- `hasrelation.<relationrange>.{$faction}` → `true iff the relation to other faction is in specified range`
- `relationto.{$component}` → `Relation to owner of $component`
- `relationto.{$faction}` → `Relation to other faction`
- `defaultrelationto.{$faction}` → `Default relation to other faction before any changes`
- `doesrelationrangechange.{$numeric}.{$numeric}` → `true iff relation range changes between two relation values`
- `isrelationlocked` → `true iff relations are locked`
- `isdiplomacyactive` → `true iff diplomacy is active`
- `arediplomacyeventsallowed` → `true iff allowed to feature in diplomacy events`
- `isdiplomacyexcluded.{$faction}` → `true iff diplomacy is currently excluded between this faction and the other faction`
- `mayattack.{$component}` → `true if this faction has a kill relation towards other component, or has a killmilitary relation and the other component has the purpose 'fight' (can be overridden by fire authorisation override)`
- `mayattack.{$faction}` → `true if this faction has a kill relation towards the faction (can be overridden by fire authorisation override)`
- `ishostileto.{$component}` → `true if mutual faction and object relations and fire authorisations allow either side to attack (see mayattack)`
- `ishostileto.{$faction}` → `true if faction relations and fire authorisations allow either side to attack (see mayattack)`
- `haslicence.<licencetype>.{$faction}` → `true iff faction has licence of specified type and faction`
- `canholdlicence.{$licence}` → `true iff faction is currently allowed to hold $licence, based on minrelation and precursor properties`
- `canholdlicence.<licencetype>.{$faction}` → `true iff faction is currently allowed to hold licence of specified type and faction, based on minrelation and precursor properties`
- `licences` → `List of own licences`
- `heldlicences` → `List of held licences`
- `licence.<licencetype>` → `Licence value of the specified type for the faction. (May result in licence which fails .exists)`
- `mood.<moodtype>` → `Current mood level of the specified mood type`
- `defaultmood.<moodtype>` → `Default mood level of the specified mood type`
- `isaggressive` → `true iff this faction is aggressive`
- `iseconomic` → `true iff this faction has a focus on economics`
- `ispolice` → `true iff this faction can act as a law enforcement faction`
- `isprotective` → `true iff this faction will intervene if 3rd party units are attacked nearby`
- `isvisitor` → `true iff this faction is an online visitor`
- `money` → `Money in the faction's account`
- `hasownaccount` → `true iff faction has its own account (uses dummy account with large random sum otherwise)`
- `willclaimspace` → `true iff this faction will claim/contest space if it owns a station which can grant ownership`
- `tags` → `List of faction tags`
- `hastag.{$tag}` → `Does the specified tag exist in the tags for this faction`
- `hastag.<tagname>` → `Shortcut for hastag.{tag.<tagname>}`
- `representative` → `Given faction representative or null`
- `diplomat` → `Given faction diplomat or null`
- `headquarters` → `Given faction's headquarters station or null`
- `icon` → `Returns the name of the active faction icon as it is called in the IconLibrary`
- `doesresupply` → `true iff this faction will resupply ships at equipment docks, shipyards or resupplier ships`

## `race` — inherits `dbdata` (12 direct properties)

- `id` → `ID`
- `name` → `Name`
- `rawname` → `Raw name, as text entry reference`
- `shortname` → `Short name`
- `spacename` → `Space name`
- `homespacename` → `Home space name`
- `description` → `Description`
- `height` → `Default height for characters of this race`
- `facecutscene` → `Face cutscene key for this race, or null if no default is defined`
- `workforce.resources` → `Resoures needed for the workforce of this race to prosper`
- `agent.icon` → `Default icon for agents of this race`
- `agent.femaleicon` → `Icon for female agents of this race`

## `ware` — inherits `dbdata` (79 direct properties)

- `id` → `ID`
- `name` → `Name`
- `rawname` → `Raw name, as text entry reference`
- `description` → `Description`
- `icon` → `Icon ID`
- `minprice` → `Minimum price`
- `averageprice` → `Average price`
- `maxprice` → `Maximum price`
- `pricerange` → `Price range`
- `volume` → `Volume of this ware`
- `waretransport` → `Transport type of this ware`
- `transporttag` → `Transport type tag of this ware`
- `buyrestriction.base` → `Base notoriety restriction to buy the ware`
- `buyrestriction.{$faction}` → `Notoriety restriction to buy the ware from a faction`
- `sellrestriction.base` → `Base notoriety restriction to sell the ware`
- `sellrestriction.{$faction}` → `Notoriety restriction to sell the ware to a faction`
- `tags` → `List of ware tags`
- `hastag.{$tag}` → `Does the specified tag exist in the ware tags for this ware`
- `hastag.<tagname>` → `Shortcut for hastag.{tag.<tagname>}`
- `hasanytag.{$list}` → `true iff this ware's tags contain any tag from the list`
- `hasalltags.{$list}` → `true iff this ware's tags contain all tags from the list`
- `isinventory` → `true iff ware is inventory`
- `isammo` → `true iff ware is an ammo ware`
- `iscargo` → `true iff ware is normal cargo, i.e. not inventory or an ammo ware`
- `iscrafting` → `true iff ware is a crafting ware`
- `isdeployable` → `true iff ware is a deployable`
- `isvolatile` → `true iff ware is volatile`
- `isgift` → `true iff ware is a gift`
- `israre` → `true iff ware is rare`
- `isdropallowed` → `true iff dropping this ware is allowed`
- `isresearchable` → `true iff this ware can be researched`
- `group.id` → `Ware group id`
- `group.name` → `Ware group name`
- `group.rawname` → `Ware group raw name, as text entry reference`
- `group.description` → `Ware group description`
- `group.icon` → `Ware group icon ID`
- `group.factory.name` → `Ware group factory name`
- `group.factory.rawname` → `Ware group factory raw name, as text entry reference`
- `group.factory.description` → `Ware group factory description`
- `group.tags` → `List of ware group tags`
- `group.hastag.{$tag}` → `Does the specified tag exist in the ware group tags for this ware`
- `group.hastag.<tagname>` → `Shortcut for hastag.{tag.<tagname>}`
- `group.hasanytag.{$list}` → `true iff this ware group's tags contain any tag from the list`
- `group.hasalltags.{$list}` → `true iff this ware group's tags contain all tags from the list`
- `group.isbuildable` → `true iff ware group can be built`
- `group.istradable` → `true iff ware group can be traded`
- `group.iscraftable` → `true iff ware group can be crafted or used for crafting`
- `group.tier` → `Ware group tier`
- `group.priority` → `Ware group priority`
- `container` → `Container macro for this ware`
- `illegal` → `true iff ware is illegal to any faction`
- `illegalto.{$faction}.{null}` → `true iff ware is illegal to $faction`
- `illegalto.{$faction}.{$faction}` → `true iff ware is illegal to first $faction, taking into account licences held by second $faction`
- `objectmacro` → `Macro of Ware Object (if defined)`
- `objectcount` → `Amount of ware object`
- `products` → `All product wares (all production methods) that this ware is a resource for`
- `resources` → `All resource wares (default method)`
- `raceresources.{$race}` → `All resource wares using the provided race' production method (defaults to the default method if the race does not have an overriding method)`
- `issoftware` → `true iff ware is tagged as software`
- `softwareversion.base` → `Base version of a software type, e.g. base of software_scannerobjectmk3 is software_scannerobjectmk1`
- `softwareversion.max` → `Highest version of a software type, e.g. software_scannerobjectmk3 is the latest version of software_scannerobjectmk1`
- `softwareversion.next` → `Next higher version of a software type, e.g. software_dockmk1 is followed by software_dockmk2`
- `softwareversion.previous` → `Previous version of a software type, e.g. software_dockmk2 is preceded by software_dockmk1`
- `isweaponmod` → `true iff ware is primary ware for a weapon mod`
- `isenginemod` → `true iff ware is primary ware for an engine mod`
- `isshieldmod` → `true iff ware is primary ware for a shield mod`
- `isshipmod` → `true iff ware is primary ware for a ship mod`
- `isequipmentmod` → `true iff ware is primary ware for any type of equipment mod`
- `equipmentmodquality` → `quality level of equipment mod for which this is primary ware, if any`
- `ispaintmod` → `true iff ware is a paint mod`
- `paintmodquality` → `quality level of paint mod, if this is ware is a a paint mod`
- `isclothingmod` → `true iff ware is a clothing mod`
- `clothingmodquality` → `quality level of clothing mod, if this is ware is a a clothing mod`
- `research.unlocked` → `true iff this this ware has been researched by the player`
- `research.precursors` → `Research precursors to research this ware`
- `research.requiredprecursors` → `Research precursors required to unlock access to ware`
- `research.resources` → `Resources needed to process the research`
- `isprocessed` → `true iff ware is processed, e.g. raw scrap`
- `videomacro` → `Video macro of Ware (if defined, will fall back to $ware.objectmacro otherwise)`

## `lookuplist` (4 direct properties)

- `count` → `Number of lookup entries`
- `{$index}` → `Lookup entry at index position`
- `list` → `All lookup entries as a script list`
- `random` → `Random lookup entry`

## `warelist` (6 direct properties)

- `list` → `All wares as a script list`
- `random` → `Random ware (at least one ware must be present)`
- `count` → `Number of wares`
- `{$numeric}` → `The $numeric-th ware in the ware list (1-based)`
- `{$ware}.exists` → `true iff $ware is in the ware list`
- `illegalto.{$faction}` → `true iff there are wares illegal to $faction, taking into account licences held by the ware owner, if applicable`

## `wareamountlist` (9 direct properties)

- `list` → `All wares with non-zero amount as a script list`
- `table` → `All wares and amounts with non-zero amount as a script table`
- `random` → `Random ware (at least one ware with non-zero amount must be present)`
- `count` → `Number of different wares with non-zero amount`
- `illegal` → `true iff there is an illegal ware`
- `illegalto.{$faction}` → `true iff there are wares illegal to $faction, taking into account licences held by the ware owner, if applicable`
- `{$numeric}` → `The $numeric-th ware in the ware-amount list (1-based)`
- `{$ware}.exists` → `true iff there is a non-zero amount of $ware`
- `{$ware}.count` → `Number of wares of type $ware`

## `cargolist` — inherits `wareamountlist` (7 direct properties)

- `{$ware}.free` → `Amount of $ware that can be added to the cargo`
- `{$ware}.max` → `Maximum amount of $ware in the cargo (ignoring existing cargo)`
- `tags` → `Compatible ware tags of the container`
- `hastag.{$tag}` → `Is the container compatible with the specified ware tag?`
- `hastag.<tagname>` → `Shortcut for hastag.{tag.<tagname>}`
- `hasanytag.{$list}` → `true iff the compatible ware tags for this container contain any tag from the list`
- `hasalltags.{$list}` → `true iff the compatible ware tags for this container contain all tags from the list`

## `containercargolist` — inherits `cargolist` (14 direct properties)

- `free.all` → `Total free cargo volume remaining, regardless of waretransport type`
- `free.condensate` → `Total free cargo volume remaining for condensate`
- `free.container` → `Total free cargo volume remaining for containers`
- `free.liquid` → `Total free cargo volume remaining for liquids`
- `free.solid` → `Total free cargo volume remaining for solids`
- `free.universal` → `Total free universal cargo volume remaining`
- `free.{$tag}` → `Total free cargo volume remaining for the specified ware transport tag`
- `capacity.all` → `Total cargo volume available, regardless of waretransport type`
- `capacity.condensate` → `Total condensate cargo volume available`
- `capacity.container` → `Total container cargo volume available`
- `capacity.liquid` → `Total liquid cargo volume available`
- `capacity.solid` → `Total solid cargo volume available`
- `capacity.universal` → `Total universal cargo volume available`
- `capacity.{$tag}` → `Total cargo volume available for the specified ware transport tag`

## `modulecargolist` — inherits `cargolist` (2 direct properties)

- `free` → `Total free cargo volume remaining`
- `capacity` → `Total cargo volume available`

## `npctemplate` (0 direct properties)


## `npctemplateentry` (22 direct properties)

- `exists` → `true iff NPC template exists`
- `seed` → `Persistent pseudo-random seed used to generate and identify the NPC`
- `macro` → `Macro of the NPC`
- `name` → `Name of the NPC`
- `race` → `The NPC's race`
- `page` → `Voice text page ID`
- `isfemale` → `Is NPC female`
- `role` → `The NPC's role`
- `ismissionactor` → `Is a mission NPC`
- `isintransit` → `Is the entity in transit to a location?`
- `isbusy` → `Is the entity flagged as busy?`
- `istransferscheduled` → `Is a crew transfer order scheduled for the entity?`
- `istemporary` → `Is the entity temporary?`
- `podarrivaltime` → `Scheduled time of arrival at current object in a crew transfer pod, or null if not being transferred via pod`
- `isremotecommable` → `Is NPC remote commable (only relevant for NPC actors, not NPC templates and is automatically set when NPC is instanced and unset when creating a template)`
- `customhandler` → `true iff the NPC has a custom conversation handler`
- `skill.{$skilltype}` → `Skill value between 0 and 15 of the supplied skill type`
- `skill.<skillname>` → `Shortcut for skill.{skilltype.<skillname>}`
- `combinedskill` → `Combined skill value between 0 and 100, based on weighted skills that are relevant for the NPC's role`
- `potentialskill.{$entityrole}` → `Potential combined skill value between 0 and 100, based on weighted skills that are relevant for the role`
- `potentialskill.{$controlpost}` → `Potential combined skill value between 0 and 100, based on weighted skills that are relevant for the control post`
- `tradesvisible` → `true iff the NPC's trades are visible to the player`

## `macro` — inherits `dbdata` (82 direct properties)

- `id` → `ID (internal macro name). But instead of comparing macro IDs, it is recommended to use ismacro.{$macro}`
- `name` → `Display name`
- `rawname` → `Raw display name, as text entry reference`
- `description` → `Description`
- `extension` → `Source extension id`
- `isextensionpersonal` → `true iff the source extension is personal`
- `class` → `Component class`
- `isclass.{$class}` → `true iff the macro is of the given class`
- `isclass.<classname>` → `Shortcut for isclass.{class.<classname>}`
- `isclass.{$list}` → `true iff the macro is of one of the classes from the list`
- `ismacro.{$macro}` → `true iff the macro is the specified macro or derived from it ($macro must originate from a macro.<name> lookup)`
- `ismacro.<macroname>` → `Shortcut for ismacro.{macro.<macroname>}`
- `ismacro.{$list}` → `true iff the macro is one of the specified macros or derived from one of them (macros in list must originate from a macro.<name> lookup)`
- `icon` → `Icon ID (e.g. of missile), or null if not applicable`
- `makerraces` → `The macro's maker race list (destructible macros only)`
- `primarypurpose` → `The macro's primary purpose (destructible macros only)`
- `threatscore` → `The macro's threat score, either defined by the macro itself or by defaults based on its primary purpose (destructible macros only)`
- `docksize` → `Tag of required dock size (ship macros only)`
- `docksizes` → `List of tags of supported dock sizes (dockingbay macros only)`
- `numdocks.{$docksize}` → `Number of connected dockingbays supporting the specified docksize (module macros only)`
- `numpierdocks` → `Number of connected capital ship dock locations (pier macros only)`
- `isstorage` → `true iff this is an internal storage bay (dockingbay macros only)`
- `ware` → `Ware linked to this macro`
- `isunit` → `true iff the macro is a unit`
- `isdeployable` → `true iff the macro is a deployable`
- `islasertower` → `true iff the macro is a lasertower`
- `canhaveattackablemodules` → `true iff the ship is defined to contain a defence module which indicates it may have targetable modules (ship macros only)`
- `unitcategory` → `Unit category this macro belongs to (null if none, only valid for units defined in loadoutrules.xml)`
- `deployablecategory` → `Deployable category this macro belongs to (null if none, only valid for deployables defined in loadoutrules.xml)`
- `boundingbox.exists` → `Whether this macro's bounding box has non-zero dimensions`
- `boundingbox.max` → `Maximum bounds of this macro's bounding box`
- `boundingbox.center` → `Center position of this macro's bounding box`
- `workforce.capacity` → `Workforce capacity for given macro`
- `workforce.race` → `Workforce race a given macro supports`
- `workforce.optimal` → `Number of workers required for given macro to operate at peak efficiency`
- `workforce.min` → `Number of workers required for given macro to operate`
- `products` → `All produced wares`
- `productionvolume` → `The volume of all wares produced by a production module in one hour`
- `consumptionvolume` → `The volume of all wares consumed by a production module in one hour`
- `cargocapacity` → `The storage capacity of a storage module macro (legacy - use $macro.cargo.capacity.all)`
- `cargo.capacity.all` → `Total cargo volume available, regardless of waretransport type (storagemodule and container macros only)`
- `cargo.capacity.condensate` → `Total condensate cargo volume available (storagemodule and container macros only)`
- `cargo.capacity.container` → `Total container cargo volume available (storagemodule and container macros only)`
- `cargo.capacity.liquid` → `Total liquid cargo volume available (storagemodule and container macros only)`
- `cargo.capacity.solid` → `Total solid cargo volume available (storagemodule and container macros only)`
- `cargo.capacity.universal` → `Total universal cargo volume available (storagemodule and container macros only)`
- `cargo.capacity.{$tag}` → `Total cargo volume available for the specified ware transport tag (storagemodule and container macros only)`
- `cargo.{$ware}.max` → `Maximum amount of $ware which can be contained (storagemodule and container macros only)`
- `cargo.tags` → `Compatible ware tags of the macro (storagemodule macros only)`
- `cargo.hastag.{$tag}` → `Does the specified tag exist as a compatible ware tag for this storage module (storagemodule macros only)`
- `cargo.hastag.<tagname>` → `Shortcut for cargo.hastag.{tag.<tagname>} (storagemodule macros only)`
- `cargo.hasanytag.{$list}` → `true iff the compatible ware tags for this storage module contain any tag from the list (storagemodule macros only)`
- `cargo.hasalltags.{$list}` → `true iff the compatible ware tags for this storage module contain all tags from the list (storagemodule macros only)`
- `waretransport` → `List of waretransport types which can be carried by this macro (storagemodule and container macros only)`
- `transportunitcapacity.cargo` → `Cargo transport capacity if this macro is a transport unit`
- `transportunitcapacity.missiles` → `Missile transport capacity if this macro is a transport unit`
- `transportunitcapacity.units` → `Unit transport capacity if this macro is a transport unit`
- `isbuildingallowed` → `true if building is allowed at this dock (dockingbay macros only)`
- `istradingallowed` → `true if trading is allowed at this dock (dockingbay macros only)`
- `isplayeronly` → `true if this dock is exclusively used for the player (dockingbay macros only)`
- `isshowroom` → `true if this dock is exclusively used as a showroom (dockingbay macros only)`
- `isventureronly` → `true if this dock is exclusively used for venturers (dockingbay macros only)`
- `isventuremodule` → `true if this module is for use with venture platforms (dockarea and connection macros only)`
- `isheadquarters` → `true if this station is a headquarters (station macros only)`
- `ispiratebase` → `true if this station is a pirate base (station macros only)`
- `isfriendfoe` → `true if this mine has a friend/foe feature (mine macros only)`
- `isfemale` → `true if this macro is female (entity macros only)`
- `canclaimownership` → `true iff this macro can claim ownership of a sector`
- `hascontrolpanel.{$controlpaneltype}` → `true if this room has a control panel of the specified type (room macros only)`
- `maxradarrange` → `Maximal radar range`
- `people.capacity` → `Maximum amount of potential space on board for people as NPC templates (controllable only)`
- `isdatavault` → `true iff the macro is a Data Vault`
- `islandmark` → `true iff the macro is a landmark`
- `explosiondamage.total` → `Total potential damage this macro can do if it explodes. (explosive macros only e.g. such as missiles)`
- `explosiondamage.hullshield` → `Total potential damage this macro can do if it explodes. Damage is dealt to shields if present, otherwise to hull. (explosive macros only e.g. missiles)`
- `explosiondamage.hullonly` → `Total potential damage this macro can do if it explodes. Damage is dealt directly to hull despite shields being present. (explosive macros only e.g. missiles)`
- `explosiondamage.shieldonly` → `Total potential damage this macro can do if it explodes. Damage is dealt only to shields. (explosive macros only e.g. missiles)`
- `explosiondamage.hullnoshield` → `Total potential damage this macro can do if it explodes. Damage is dealt only to hull and only if no shields are present. (explosive macros only e.g. missiles)`
- `isbeam` → `true if this weapon fires a beam or this is a beam bullet. (weapon and bullet macros only)`
- `isguided` → `true if this explosive is guided or this weapon fires a guided explosive. (explosive and weapon macros only e.g. missiles, missilelaunchers or missileturrets)`
- `istorpedo` → `true if this explosive is a torpedo or this weapon fires a torpedo. (explosive and weapon macros only e.g. missiles, missilelaunchers or missileturrets)`
- `countermeasureresistance.{$macro}` → `percentage change of this explosive macro resisting the effects of the provided countermeasure macro (explosive macros only e.g. missiles)`

## `unlock` — inherits `dbdata` (14 direct properties)

- `id` → `ID`
- `name` → `Name`
- `rawname` → `Raw name, as text entry reference`
- `description` → `Description`
- `allowedowners` → `List of allowed owner faction based on who owns the object where this unlock is triggered (empty list = all factions allowed)`
- `allowedwares` → `List of allowed wares for tradeoffer location unlocks (empty list = all wares allowed)`
- `minrelation` → `Minimum relation with owner for this unlock to be triggered`
- `maxrelation` → `Maximum relation with owner for this unlock to be triggered`
- `secrecylevel.min` → `Minimum secrecy level of component for this unlock to be triggered`
- `secrecylevel.max` → `Maximum secrecy level of component for this unlock to be triggered`
- `isblueprint` → `true iff this unlock relates to a blueprint ware`
- `iscommission` → `true iff this unlock relates to a trade commission`
- `isdiscount` → `true iff this unlock relates to a trade discount`
- `isinformation` → `true iff this unlock relates to revealing information`

## `missiongroup` — inherits `dbdata` (6 direct properties)

- `id` → `ID`
- `name` → `Name of the mission group`
- `rawname` → `Raw name of the mission group, as text entry reference`
- `description` → `Description of the mission group`
- `faction` → `Primary faction`
- `enemy` → `Enemy faction`

## `notification` — inherits `dbdata` (5 direct properties)

- `id` → `ID`
- `name` → `Name of the notification type`
- `rawname` → `Raw name of the notification type, as text entry reference`
- `description` → `Description of the notification type`
- `active` → `Are notifications of this type enabled?`

## `tag` (0 direct properties)


## `cue` (23 direct properties)

- `exists` → `true iff cue exists`
- `name` → `Cue name (unqualified)`
- `version` → `Version`
- `time` → `Time of cue activation (or time of last time actions were performed, if the active cue is waiting for a subsequent actions block`
- `state` → `Current cue state`
- `parent` → `Parent cue, or null if this is a root cue`
- `static` → `The instantiating cue if applicable, otherwise null`
- `staticbase` → `The static cue used as base for this cue (same as this if this is not an instance)`
- `namespace` → `Namespace cue`
- `library` → `If cue is a library reference, the base library cue`
- `isinstance` → `true iff cue is an instance`
- `hasmissionoffer` → `true iff cue has a mission offer`
- `hasmission` → `true iff cue has a mission`
- `hasguidance` → `true iff guidance is active for this cue's mission`
- `offerlocations` → `List of all component slots used as offer locations for this cue's mission offer`
- `canactivatesubmission.{$cue}` → `true iff a submission of this mission thread is allowed to be activated`
- `missiontype` → `the mission type of this cue's mission`
- `missionendtime` → `the end time of this cue's mission if the mission itself has a time limit, otherwise null (NOTE: not to be confused with a mission objective endtime, which is a separate value)`
- `objective` → `the objective type of this cue's mission`
- `objectiveendtime` → `the end time of the current objective of this cue's mission if the current objective has a time limit, otherwise null`
- `actor` → `Last associated actor, or null`
- `actors` → `List of all associated actors`
- `$<variable>` → `Value of cue variable`

## `enum` (0 direct properties)


## `kwenum` (0 direct properties)


## `dbdata` (0 direct properties)


## `class` — inherits `enum` (3 direct properties)

- `isclass.{$class}` → `true iff this class is of the given class`
- `isclass.<classname>` → `Shortcut for isclass.{class.<classname>}`
- `isclass.{$list}` → `true iff this class is of one of the classes in the list`

## `componentstate` — inherits `enum` (0 direct properties)


## `killmethod` — inherits `enum` (0 direct properties)


## `attention` — inherits `enum` (0 direct properties)


## `flightbehaviour` — inherits `enum` (0 direct properties)


## `flightcontrolmodel` — inherits `enum` (0 direct properties)


## `formationshape` — inherits `enum` (0 direct properties)


## `activity` — inherits `enum` (0 direct properties)


## `objective` — inherits `enum` (0 direct properties)


## `missiontype` — inherits `enum` (0 direct properties)


## `level` — inherits `enum` (0 direct properties)


## `alertlevel` — inherits `enum` (0 direct properties)


## `command` — inherits `enum` (0 direct properties)


## `commandaction` — inherits `enum` (0 direct properties)


## `cuestate` — inherits `kwenum` (0 direct properties)


## `dronemode` — inherits `enum` (0 direct properties)


## `roompopulationtype` — inherits `enum` (0 direct properties)


## `moodlevel` — inherits `enum` (0 direct properties)


## `orderstate` — inherits `enum` (0 direct properties)


## `weaponmode` — inherits `enum` (0 direct properties)


## `dockstate` — inherits `enum` (0 direct properties)


## `quadrant` — inherits `kwenum` (1 direct properties)

- `inverse` → `the opposite direction of the quadrant`

## `datatype` — inherits `kwenum` (2 direct properties)

- `isnumeric` → `true iff the data type is non-null and numeric - example: (typeof $value).isnumeric`
- `isstring` → `true iff the data type is a string - example: (typeof $value).isstring`

## `entitytype` — inherits `dbdata` (4 direct properties)

- `name` → `Default name of the entity type`
- `rawname` → `Raw default name of the entity type, as text entry reference`
- `description` → `Description of the entity type`
- `icon` → `Icon ID of the entity type`

## `entityrole` — inherits `dbdata` (14 direct properties)

- `name` → `Default name of the entity role`
- `rawname` → `Raw default name of the entity role, as text entry reference`
- `femalename` → `Female name of the entity role`
- `pluralname` → `Plural name of the entity role`
- `description` → `Description of the entity role`
- `tag` → `Defined tag for this role`
- `type` → `Entity type for this role`
- `hirable` → `Can this entity role be hired`
- `isindependent` → `whether ownership of person assigned to this role is independent of ownership of object to which they are assigned`
- `tiers` → `List of tier level values as integers`
- `tier.{$level}.name` → `Name of the tier at this level`
- `tier.{$level}.rawname` → `Raw name of the tier at this level, as text entry reference`
- `tier.{$level}.level` → `Lowerbound level value of the tier at the provided level`
- `icon` → `Icon ID of the entity role`

## `skilltype` — inherits `enum` (2 direct properties)

- `name` → `Skill name`
- `ware` → `Skill upgrade ware associated with this skill type`

## `controlpost` — inherits `dbdata` (10 direct properties)

- `name` → `Default name of the control post`
- `rawname` → `Raw default name of the control post, as text entry reference`
- `description` → `Description of the control post`
- `icon` → `Icon ID of the control post`
- `type` → `Entity type of the control post`
- `tag` → `Defined tag for this control post`
- `skilltypes` → `List of relevant skill types`
- `skillrelevance.{$skilltype}` → `Contribution of the supplied skill to the entity's combined skill in percent, see $entity.combinedskill`
- `skillrelevance.<skillname>` → `Shortcut for skillrelevance.{skilltype.<skillname>}`
- `isindependent` → `whether ownership of person assigned to this post is independent of ownership of object to which they are assigned`

## `assignment` — inherits `dbdata` (4 direct properties)

- `name` → `Name of the assignment`
- `rawname` → `Raw name of the assignment, as text entry reference`
- `description` → `Description of the assignment`
- `icon` → `Icon ID of the assignment`

## `purpose` — inherits `dbdata` (4 direct properties)

- `name` → `Name of the purpose`
- `rawname` → `Raw name of the purpose, as text entry reference`
- `description` → `Description of the purpose`
- `parent` → `Parent purpose`

## `controlposition` — inherits `enum` (1 direct properties)

- `tag` → `Defined tag used as the group for this control position`

## `unitcategory` — inherits `enum` (3 direct properties)

- `name` → `Name of the unit category`
- `maxmk` → `Maximum mk for this unit category`
- `mk.{$i}.list` → `List of unit macros of the category and mk`

## `deployablecategory` — inherits `enum` (3 direct properties)

- `name` → `Name of the deployable category`
- `maxmk` → `Maximum mk for this deployable category`
- `mk.{$i}.list` → `List of deployable macros of the category and mk`

## `controlpaneltype` — inherits `enum` (2 direct properties)

- `name` → `Name of control panel type`
- `requireditems` → `Required items for hacking`

## `signalleaktype` — inherits `enum` (0 direct properties)


## `roomtype` — inherits `enum` (0 direct properties)


## `boardingphase` — inherits `enum` (0 direct properties)


## `boardingbehaviour` — inherits `enum` (0 direct properties)


## `blacklisttype` — inherits `enum` (0 direct properties)


## `blacklistgroup` — inherits `enum` (0 direct properties)


## `agenttype` — inherits `enum` (0 direct properties)


## `agentrisk` — inherits `enum` (0 direct properties)


## `agentresult` — inherits `enum` (0 direct properties)


## `waretransport` — inherits `enum` (2 direct properties)

- `name` → `Name of ware transport type`
- `tag` → `Corresponding transport type tag for checking storage compatibility`

## `relationchangereason` — inherits `enum` (1 direct properties)

- `name` → `Name of the relation change reason`

## `shiptype` — inherits `enum` (2 direct properties)

- `name` → `Name of the ship type`
- `description` → `Description of the ship type`

## `stationtype` — inherits `enum` (0 direct properties)


## `regiongroup` — inherits `enum` (0 direct properties)


## `influence` — inherits `enum` (3 direct properties)

- `name` → `Name of the influence level`
- `min` → `The minimum value of this influence level`
- `max` → `The maximum value of this influence level`

## `numeric` (0 direct properties)


## `integer` — inherits `numeric` (0 direct properties)


## `boolean` — inherits `integer` (0 direct properties)


## `money` — inherits `numeric` (2 direct properties)

- `formatted.{$string}` → `Formatted money string, expanding tags in format string into corresponding values - example: $money.formatted.{'%6cs %Cr'}`
- `formatted.default` → `Formatted money string in default format (%s), with full accuracy, without cents`

## `largeint` — inherits `numeric` (0 direct properties)


## `float` — inherits `numeric` (0 direct properties)


## `length` — inherits `numeric` (0 direct properties)


## `angle` — inherits `numeric` (0 direct properties)


## `hitpoints` — inherits `numeric` (0 direct properties)


## `time` — inherits `numeric` (2 direct properties)

- `formatted.{$string}` → `Formatted time string, expanding tags in format string into corresponding values - example: $time.formatted.{'%m:%S'}`
- `formatted.default` → `Formatted time string in default format (%T). Days are only displayed if the time is at least 1d.`

## `largefloat` — inherits `numeric` (0 direct properties)

