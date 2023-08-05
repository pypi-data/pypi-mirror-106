========
RefStack
========

What is RefStack?
#################

- Toolset for testing interoperability between OpenStack clouds.
- Database backed website supporting collection and publication of
  Community Test results for OpenStack.
- User interface to display individual test run results.

Overview
########

RefStack intends on being THE source of tools for interoperability testing
of OpenStack clouds.

RefStack provides users in the OpenStack community with a Tempest wrapper,
refstack-client, that helps to verify interoperability of their cloud
with other OpenStack clouds. It does so by validating any cloud
implementation against the OpenStack Tempest API tests.

**RefStack and Interop Working Group** - The prototypical use case for RefStack
provides the Interop Working Group - formerly known as DefCore committee - the
tools for vendors and other users to run API tests against their clouds to
provide the WG with a reliable overview of what APIs and capabilities are
being used in the marketplace. This will help to guide the Interop
Working Group defined capabilities and help ensure interoperability across
the entire OpenStack ecosystem. It can also be used to validate clouds
against existing capability lists, giving you assurance that your cloud
faithfully implements OpenStack standards.

**Value add for vendors** - Vendors can use RefStack to demonstrate that
their distros, and/or their customers' installed clouds remain with OpenStack
after their software has been incorporated into the distro or cloud.

**RefStack consists of two parts:**

* **refstack-api**
   Our API isn't just for us to collect data from private and public cloud
   vendors. It can be used by vendors in house to compare interoperability
   data over time.

   * API and UI install docs: https://opendev.org/osf/refstack/src/master/doc/source/refstack.rst
   * repository: https://opendev.org/osf/refstack
   * reviews: https://review.opendev.org/#/q/status:open+project:osf/refstack

* **refstack-client**
   refstack-client contains the tools you will need to run the
   Interop Working Group tests.

   * repository: https://opendev.org/osf/refstack-client
   * reviews: https://review.opendev.org/#/q/status:open+project:osf/refstack-client

Get involved!
#############

* Mailing List: openstack-discuss@lists.openstack.org
* IRC: #refstack on Freenode
* Wiki: https://wiki.openstack.org/wiki/Governance/InteropWG
* Meetings: See the wiki page for meeting info
* Web-site: https://refstack.openstack.org
