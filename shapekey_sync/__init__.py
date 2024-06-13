# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "ShapeKey Sync",
    "author" : "Enik Bignolin", 
    "description" : "idk, it sets suff",
    "blender" : (4, 1, 0),
    "version" : (1, 0, 4),
    "location" : "",
    "warning" : "",
    "doc_url": "", 
    "tracker_url": "", 
    "category" : "Mesh" 
}


import bpy
import bpy.utils.previews


addon_keymaps = {}
_icons = None
visual_scripting_editor = {'sna_objectcollection': None, 'sna_witch_collection': None, }


def sna_update_sna_shapekey_value_A100C(self, context):
    sna_updated_prop = self.sna_shapekey_value
    if (bpy.context.scene.sna_witch_collection == None):
        visual_scripting_editor['sna_witch_collection'] = bpy.context.scene.collection
    else:
        visual_scripting_editor['sna_witch_collection'] = bpy.context.scene.sna_witch_collection
    if bpy.context.scene.sna_allobject:
        visual_scripting_editor['sna_objectcollection'] = visual_scripting_editor['sna_witch_collection'].all_objects
    else:
        visual_scripting_editor['sna_objectcollection'] = visual_scripting_editor['sna_witch_collection'].objects
    for i_9DF98 in range(len(visual_scripting_editor['sna_objectcollection'])):
        if property_exists("bpy.data.objects[getattr(visual_scripting_editor['sna_objectcollection'][i_9DF98], 'name', None)].data.shape_keys.key_blocks[bpy.data.objects[str(bpy.context.active_object.name)].data.shape_keys.key_blocks[bpy.data.objects[getattr(bpy.context.active_object, 'name', None)].active_shape_key_index].name].value", globals(), locals()):
            bpy.data.objects[getattr(visual_scripting_editor['sna_objectcollection'][i_9DF98], 'name', None)].data.shape_keys.key_blocks[bpy.data.objects[str(bpy.context.active_object.name)].data.shape_keys.key_blocks[bpy.data.objects[getattr(bpy.context.active_object, 'name', None)].active_shape_key_index].name].value = bpy.context.scene.sna_shapekey_value


def property_exists(prop_path, glob, loc):
    try:
        eval(prop_path, glob, loc)
        return True
    except:
        return False


class SNA_PT_SHAPEKEY_SYNC_A8659(bpy.types.Panel):
    bl_label = 'ShapeKey Sync'
    bl_idname = 'SNA_PT_SHAPEKEY_SYNC_A8659'
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'data'
    bl_category = 'New Category'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        row_55375 = layout.row(heading='', align=True)
        row_55375.alert = False
        row_55375.enabled = True
        row_55375.active = True
        row_55375.use_property_split = False
        row_55375.use_property_decorate = False
        row_55375.scale_x = 1.0
        row_55375.scale_y = 1.0
        row_55375.alignment = 'Expand'.upper()
        row_55375.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_55375.prop_search(bpy.context.scene, 'sna_witch_collection', bpy.data, 'collections', text='', icon='NONE')
        row_55375.prop(bpy.context.scene, 'sna_allobject', text='allObject', icon_value=0, emboss=True, toggle=True)
        layout.prop(bpy.context.scene, 'sna_shapekey_value', text='', icon_value=0, emboss=True, slider=True)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.types.Scene.sna_shapekey_value = bpy.props.FloatProperty(name='shapekey_value', description='', default=0.0, subtype='NONE', unit='NONE', min=0.0, max=1.0, step=3, precision=6, update=sna_update_sna_shapekey_value_A100C)
    bpy.types.Scene.sna_witch_collection = bpy.props.PointerProperty(name='witch collection', description='if blank, it will defaulted to the Scene Collection', type=bpy.types.Scene)
    bpy.types.Scene.sna_allobject = bpy.props.BoolProperty(name='allObject', description='if active it will recurse to each collection inside the selected collection', default=False)
    bpy.utils.register_class(SNA_PT_SHAPEKEY_SYNC_A8659)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    del bpy.types.Scene.sna_allobject
    del bpy.types.Scene.sna_witch_collection
    del bpy.types.Scene.sna_shapekey_value
    bpy.utils.unregister_class(SNA_PT_SHAPEKEY_SYNC_A8659)
