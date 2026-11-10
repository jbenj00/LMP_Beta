# md.xsd — symbol index

Source: `schemas/md.xsd`. Entries are top-level XSD declarations, not guaranteed executable commands.

## attributeGroup (5)

- `objectivebase`
- `briefingobjective`
- `nonbriefingobjective`
- `missiondetails`
- `cue`

## complexType (19)

- `cuedoc`
- `objectiveprogress` — Objective progress data for progress bar display
- `briefingobjective` — Mission briefing objective
- `nonbriefingobjective`
- `delay` — Range of delay time between activation and performing actions (or between previous actions block and performing next actions block)
- `actions` — Cue actions
- `checkall` — List of conditions all of which must be met
- `checkany` — List of conditions any one of which must be met
- `doall` — Actions in all sub-nodes will be performed.
- `doforeach` — Traverse a list, group or table. For each element (or table key), the actions in the sub-nodes will be performed. The keyword 'loop' can be used in expressions to access data of the current iteration.
- `doany` — A randomly selected sub-node action will be performed. The chances of selection can be specified by using weights on the actions.
- `doif` — Actions in sub-nodes will be performed only if the value matches. Can be followed by <do_elseif> and/or <do_else>.
- `doelseif` — Actions in sub-nodes will be performed only if the conditions in the previous nodes are not met and if this action's values matches. Can be followed by <do_elseif> and/or <do_else>.
- `doelse` — Actions in sub-nodes will be performed only if the conditions in the previous nodes are not met.
- `dowhile` — Actions in sub-nodes will be performed in a loop while the value matches.
- `cuepatch` — Actions for patching a cue of an older version (will be performed when loading the MD script from a save). Patches are applied to waiting, active, complete or cancelled cues (see state attribute). This includes library users and instances, except for completed/cancelled instances that have already been deleted.
- `cue` — Cue
- `library` — A library cue
- `cues`

## element (1)

- `mdscript` — Mission Director script root element

## group (10)

- `missiondetails`
- `missionthreadoffer`
- `specificconditions_event`
- `specificconditions_nonevent`
- `conditions_single_nonevent`
- `conditions_single_event`
- `conditions`
- `specificactions`
- `actions`
- `cue`

## include (1)

- `common.xsd`

## simpleType (11)

- `cuename` — Cue name
- `silentobjective` — Change the objective silently? This suppresses the mission objective bar and the sound effect. Default is false
- `missiontypelookup` — Mission type
- `objectivetypelookup` — Objective action type
- `missiongrouplookup` — Mission group lookup
- `missionthreadtypelookup` — Mission thread types for missions and mission offers
- `namespacelookup` — Which cue is used as namespace?
- `todopriority` — Priority of "todo" item
- `onfaillookup` — Action when cue conditions fail (optional)
- `cuestatelookup` — Cue state
- `loadingscreenmodelookup` — Loading screen mode for next module change
