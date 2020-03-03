from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu
from menus.base import Modifier

from cms.models import Page

class TestMenu(CMSAttachMenu):

    name = _("test menu")

    def get_nodes(self, request):
        nodes = []
        n = NavigationNode(_('sample root page'), "/", 1)
        n2 = NavigationNode(_('sample settings page'), "/bye/", 2)
        n3 = NavigationNode(_('sample account page'), "/hello/", 3)
        n4 = NavigationNode(_('sample my profile page'), "/hello/world/", 4, 3)
        nodes.append(n)
        nodes.append(n2)
        nodes.append(n3)
        nodes.append(n4)
        return nodes
class UserMenu(Menu):
    def get_nodes(self, request):
            return [
                NavigationNode(_("Profile"), reverse(profile), 1, attr={'visible_for_anonymous': False}),
                NavigationNode(_("Log in"), reverse(login), 3, attr={'visible_for_authenticated': False}),
                NavigationNode(_("Sign up"), reverse(logout), 4, attr={'visible_for_authenticated': False}),
                NavigationNode(_("Log out"), reverse(logout), 2, attr={'visible_for_anonymous': False}),
            ]

class MyExampleModifier(Modifier):
    """
    This modifier makes the changed_by attribute of a page
    accessible for the menu system.
    """
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        # only do something when the menu has already been cut
        if post_cut:
            # only consider nodes that refer to cms pages
            # and put them in a dict for efficient access
            page_nodes = {n.id: n for n in nodes if n.attr["is_page"]}
            # retrieve the attributes of interest from the relevant pages
            pages = Page.objects.filter(id__in=page_nodes.keys()).values('id', 'changed_by')
            # loop over all relevant pages
            for page in pages:
                # take the node referring to the page
                node = page_nodes[page['id']]
                # put the changed_by attribute on the node
                node.attr["changed_by"] = page['changed_by']
        return nodes

class Level(Modifier):
    """
    marks all node levels
    """
    post_cut = True

    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        if breadcrumb:
            return nodes
        for node in nodes:
            if not node.parent:
                if post_cut:
                    node.menu_level = 0
                else:
                    node.level = 0
                self.mark_levels(node, post_cut)
        return nodes

    def mark_levels(self, node, post_cut):
        for child in node.children:
            if post_cut:
                child.menu_level = node.menu_level + 1
            else:
                child.level = node.level + 1
            self.mark_levels(child, post_cut)

menu_pool.register_modifier(Level)
menu_pool.register_modifier(MyExampleModifier)
menu_pool.register_menu(TestMenu)