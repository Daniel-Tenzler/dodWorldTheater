# Phase 3: Terrain RGO Modifier Limitations

## Engine Limitations Discovered

**Date:** 2026-03-23

### Issue: No Good-Specific RGO Modifiers

The original task specified adding good-specific RGO bonuses like:
```
rgo_output = {
    grain = 1.2
    coal = 1.15
}
```

**However, Victoria 2's terrain system does NOT support good-specific RGO modifiers.**

### What the Engine Supports

The terrain.txt file only supports:
- `farm_rgo_eff` - affects ALL agricultural goods (grain, cattle, fruit, fish, tea, coffee, cotton, tobacco, opium, silk, dye)
- `mine_rgo_eff` - affects ALL mining goods (coal, iron, sulphur, timber, tropical_wood, rubber, oil, precious_metal, diamond, gold)
- `farm_rgo_size` / `mine_rgo_size` - affects RGO size (POP capacity)

### Workaround Applied

Instead of good-specific bonuses, terrain-specific broad category bonuses were applied:

| Terrain | Farm RGO Eff | Mine RGO Eff | Notes |
|---------|--------------|--------------|-------|
| **farmlands** | +20% | 0% | Best for all agriculture |
| **plains** | +10% | +10% | Balanced bonus |
| **forest** | -10% | +15% | Good for timber/mining, poor for farming |
| **hills** | 0% | +10% | Mining bonus |
| **mountain** | -30% | +15% | Poor farming, good mining |
| **desert** | -20% | -20% | Harsh environment penalty |
| **new_world_plains** | +10% | +10% | Same as plains |
| **new_world_desert** | -20% | -20% | Same as desert |
| **new_world_mountain** | -30% | +15% | Same as mountain |

### Impact on Economic Balance

This creates meaningful production differences:
- **Farmlands** provinces are premium for all agricultural RGOs
- **Mountain** provinces are ideal for mining RGOs (coal, iron, sulphur, precious_metal)
- **Forest** provinces favor mining (including timber) over farming
- **Desert** provinces are consistently poor for all production

### Alternative Approaches (If Needed)

If good-specific bonuses are absolutely required, they would need to be implemented through:

1. **Province Events** - Province-specific events adding modifiers
2. **National Focus** - Country-level bonuses to specific goods in specific terrain
3. **Goods.txt Rebalancing** - Adjust base RGO output values per good (global, not terrain-specific)
4. **Tech/Invention Modifiers** - Terrain-based unlockable bonuses

However, the current broad-category approach should create sufficient differentiation for the economic rebalance goals.

### Files Modified

- `C:\Users\reffr\Documents\github\dodWorldTheater\dodWorldTheater\map\terrain.txt`

### Testing Recommendations

When testing Phase 3:
1. Check RGO output in different terrain types
2. Verify mountain provinces produce more mining goods
3. Verify farmlands provinces produce more agricultural goods
4. Compare New World vs Old World terrain consistency
