Server blacklist to block spamming XMPP / Jabber servers in ejabberd.

*spammers.yml* contains a list of known spamming XMPP servers. Based
on this *generted/blacklist.cfg* contains a ejabberd configuration in Erlang format

You can paste this verbatim into your ejabberd.cfg (legacy format) or use
include_config_file if you have a more recent version.

You also need:

    {s2s_default_policy, allow}.

to allow all other hosts.

*generated/blacklist.yml* contains the same hosts in yaml format.

If you want this list updated please create a PR to update *spammers.yml* and
have all the details in the commit message.

See this nice [talk by Mickaël Rémond][0] has more tips howto fight XMPP spam.

[0]: https://blog.process-one.net/wp-content/uploads/2016/07/Fighting-XMPP-messaging-spam-thanks-to-ejabberd-API.pdf
