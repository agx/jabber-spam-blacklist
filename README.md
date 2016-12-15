Server blacklist to block spamming XMPP / Jabber servers in ejabberd.

You can paste this verbatim into your ejabberd.cfg (legacy format) or use
include_config_file if you have a more recent version.

Yyou also need:

    {s2s_default_policy, allow}.

to allow all other hosts.

If you want this list updated please create a PR and have all the details in
the commit message.

See this nice [talk by Mickaël Rémond][0] has more tips howto fight XMPP spam.

[0]: https://blog.process-one.net/wp-content/uploads/2016/07/Fighting-XMPP-messaging-spam-thanks-to-ejabberd-API.pdf
