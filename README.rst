Readme for sciweb-tracker
------------------------------

Keeps track of requests made on a website like affiliate links, banners or visits.
Groups unique sessions together for better reporting. This is based more on following the users behavior on the site

API
====
 * ``sid``  SID is the unique session ID to map multiple tracking records to a single session to better track user behavior.
 * ``name``  A name(campaign, page, product or link name),
 * ``domain``  Domain / website (with no http:// or www)
 * ``path``  Path of the url requested
 * ``page_id`` ID of the page (Incase the name or url ever changes)
 * ``item_type``  An item type (links, banner, product, page, redirect, etc)
 * ``item_id``  ID of the item being tracked (banner, product, link, page, etc)
 * ``item_ctype``  Content Type name
 * ``counter``  Current count (will increment for duplicate requests)
 * ``ipaddress``  IP Address of the user
 * ``admin``  Admin boolean to filter out admin / testing requests from actual views
 * ``ua`` HTTP User Agent string
 * ``created`` The datetime created
 * ``redirect_to``  If redirect_to has a url, we are redirecting to that url after tracking.


