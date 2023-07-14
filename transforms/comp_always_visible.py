from srctools.logger import get_logger

from hammeraddons.bsp_transform import trans, Context, check_control_enabled

LOGGER = get_logger(__name__)


@trans('comp_always_visible')
def comp_always_visible(ctx: Context):
    """
    comp_always visible marks the visleaf it is in as visible/audible in all other visleafs, so it is always drawn/heard
    """

    for ent in ctx.bsp.ents.by_class['comp_always_visible']:
        # get visleaf the entity is in
        leaf = ctx.bsp.vis_tree().test_point(ent.get_origin())
        if leaf == None:
            origin = ent.get_origin()
            LOGGER.warn("Found comp_always_visible with no visleaf at ({}, {}, {})!", origin.x, origin.y, origin.z)
            ent.remove()
            continue

        LOGGER.debug("Found comp_always_visible in visleaf with cluster id {}", leaf.cluster_id)

        # calculate index & bitmask of the leaf in the visibility bitvector
        index = leaf.cluster_id // 8
        bitmask = 1 << (leaf.cluster_id % 8)

        # check visiblity and audibility flags
        flags = int(ent.get('spawnflags', 1))
        is_visible = (flags & 1) != 0
        is_audible = (flags & 2) != 0

        LOGGER.debug("Adding to PVS: {}, PAS: {}.", is_visible, is_audible)

        # set it to be visible/audible from all others
        for l in ctx.bsp.vis_tree().iter_leafs():
            if l == leaf or l.cluster_id == -1:
                continue

            if is_visible:
                ctx.bsp.visibility.potentially_visible[l.cluster_id][index] |= bitmask
            if is_audible:
                ctx.bsp.visibility.potentially_audible[l.cluster_id][index] |= bitmask

        # remove the entity
        ent.remove()