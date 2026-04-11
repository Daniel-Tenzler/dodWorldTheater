# Economic Rebalance Summary

**Completed:** 2026-03-23
**Approach:** Systemic Rebalance

## Changes Made

### Factory Profitability (Phase 1)
- Reduced cement/machine_parts efficiency penalties (0.5→0.3, 0.05→0.03)
- Adjusted capitalist input multiplier (-2.5→-2.0)
- Increased clerk ratio for output bonus (craftsmen/clerks 80/20→75/25)
- Fixed aeroplane_factory I/O ratio (value 0.91→1.05)

### POP Purchasing Power (Phase 2)
- Reduced life needs: farmers/labourers -15%, craftsmen -10%, clerks -5%
- Increased everyday needs: clerks +10%, craftsmen +5%
- Rebalanced goods costs: liquor 4.4→3.8, grain 2.2→2.5, fabric 2.0→2.5, steel 4.7→4.2, cotton 2.0→2.8, dye 12.0→15.0

### RGO Efficiency (Phase 3)
- Adjusted RGO hiring/firing: HIRE_HI 0.2→0.15, HIRE_LO 0.02→0.03, FIRE 0.2→0.25
- Added terrain-specific RGO bonuses: farmlands +20% farm, plains +10% both, forest -10% farm/+15% mine, hills +10% mine, mountain -30% farm/+15% mine, desert -20% both

## Results

Economic rebalance implemented. Manual testing skipped per user preference. Changes designed to improve factory profitability, POP purchasing power, and RGO efficiency through interconnected adjustments.

## Known Issues

- Manual gameplay testing not performed - user skipped testing phases
- Terrain bonuses use broad modifiers (farm_rgo_eff, mine_rgo_eff) due to V2 engine limitations
- Some terrain types (savanna, montane_forest, dryhills) may benefit from testing

## Files Modified

- dodWorldTheater/common/production_types.txt (factory templates)
- dodWorldTheater/poptypes/*.txt (POP needs)
- dodWorldTheater/common/goods.txt (goods costs)
- dodWorldTheater/common/defines.lua (RGO factors)
- dodWorldTheater/map/terrain.txt (terrain bonuses)
