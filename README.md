# StatusBot v0.1
#### By SuperShadowPlay

## Description
This bot will detect when a user updates their status in discord, and
depending on what status is specified, will give a role if the user switches
to the specified status, and will remove the role when a user switches off
the specified status.

I have not made this bot fully configurable as I would like, and plan on doing this
someday, but for now it will stay in the half-configurable state it's in.

## config.py tutorial

#### TOKEN
If you don't know what a bot token is, follow this guide:
https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token
When you have your token replace `null` with your token in the `config.py`.

#### statusDetect
For `statusDetect` the following are acceptable to replace `null` with:
`online`, `offline`, `idle`, and `dnd` (do not disturb)

#### ROLEID
For `ROLEID`, replace `null` with the ID of the role you would like to
add/remove. In order to do this, make the role able to be mentioned,
and then send a message in any channel that the role has access to.
The message should be `\@<role name>` and replace `<role name>` with the
actual name of the role.
