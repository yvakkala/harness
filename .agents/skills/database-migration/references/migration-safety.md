# Migration Safety

## Compatibility sequence

When old and new application versions may overlap, prefer staged evolution:

1. Add backward-compatible storage capability.
2. Deploy code that can operate across the transition.
3. Backfill or transform data with bounded, restartable work.
4. Verify completeness and invariant enforcement.
5. Move readers and writers to the new representation.
6. Remove obsolete storage only after the support window ends.

The exact sequence may differ, but no step should require all processes to switch atomically unless downtime is an accepted requirement.

## Verification evidence

- Migration from every supported starting version.
- Fresh schema creation.
- Representative volume, lock duration, and resource use for material tables.
- Interrupted execution and safe restart when partial progress is possible.
- Concurrent reads and writes when deployment overlaps.
- Constraint and application behavior after migration.
- Backup recency and demonstrated restore or forward-recovery path for high-risk changes.

## Destructive operations

Before authorization, state which records or fields will be lost, how many are affected, whether the loss is reversible, the verified backup or export location, the recovery sequence, expected downtime, and the exact command or release that performs the action.
