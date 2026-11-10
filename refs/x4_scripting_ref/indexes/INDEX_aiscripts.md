# aiscripts.xsd — symbol index

Source: `schemas/aiscripts.xsd`. Entries are top-level XSD declarations, not guaranteed executable commands.

## attributeGroup (1)

- `blockingaction`

## complexType (22)

- `run_script_param` — AI script parameter
- `checkall` — List of conditions all of which must be met
- `checkany` — List of conditions any one of which must be met
- `actions` — AI script actions
- `doall` — Actions in all sub-nodes will be performed.
- `doforeach` — Traverse a list, group or table. For each element (or table key), the actions in the sub-nodes will be performed. The keyword 'loop' can be used in expressions to access data of the current iteration.
- `doany` — A randomly selected sub-node action will be performed. The chances of selection can be specified by using weights on the actions.
- `doif` — Actions in sub-nodes will be performed only if the value matches. Can be followed by <do_elseif> and/or <do_else>.
- `doelseif` — Actions in sub-nodes will be performed only if the conditions in the previous nodes are not met and if this action's values matches. Can be followed by <do_elseif> and/or <do_else>.
- `doelse` — Actions in sub-nodes will be performed only if the conditions in the previous nodes are not met.
- `dowhile` — Actions in sub-nodes will be performed in a loop while the value matches.
- `interrupt_conditions`
- `interrupt_conditions_withref`
- `interrupt_actions`
- `interrupt_actions_withref`
- `interrupt_handler`
- `interrupt_handler_withref` — Global interrupt handler for this AI script and any called scripts. Can reference a library interrupt handler.
- `interrupt_library` — Library of named interrupts and interrupt conditions in global namespace
- `interrupts` — Global interrupt handlers and library definitions
- `orderdefpatch` — Patch instruction to replace the parameter of each matching existing order of an older version (will be applied when loading the order from a save). Note that this can also be necessary when adding an order parameter in a new script version, so existing orders from older saves are updated properly. By default, when parameters ar
- `orderdef` — Definition of an order, determining this AI script as the associated order script. Script parameters must be defined as order parameters. NOTE: During setup of order parameters, the script keyword "this" is only partially supported since the entity is not determined yet. "this" can only be used to access the following properties
- `aiscriptpatch` — Non-blocking AI script actions for patching a script of an older version (will be performed when loading the script from a save)

## element (1)

- `aiscript` — AI Script root element

## group (9)

- `conditions_single_nonevent`
- `conditions_single_event`
- `conditions_nonevent`
- `conditions`
- `blockingaction`
- `specificactions`
- `actionchoice`
- `actions`
- `actionswithlabel`

## include (1)

- `common.xsd`

## simpleType (13)

- `aiscriptname`
- `labelname` — Label name
- `interrupt_conditionsref` — Name of a library interrupt condition set
- `interrupt_actionsref` — Name of a library interrupt action set
- `interrupt_handlerref` — Name of a library interrupt handler
- `resumeflag` — Resume this action when an interrupt script returns, instead of resuming at a label? This has no effect if a resume attribute was specified in <run_interrupt_script>. If the action was already completed during the interrupt, the script will continue after the action immediately. Note that changing the resume attribute has no eff
- `fbehaviourlookup` — Flight behaviour
- `fcmlookup` — Flight control model
- `commandlookup` — Command
- `commandactionlookup` — Command action
- `ordercategorylookup` — Order category type
- `orderparamlookup` — Order parameter type
- `orderinputparamlookup`
