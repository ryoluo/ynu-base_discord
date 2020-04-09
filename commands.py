# coding: UTF-8


def code_block(msg):
    return "```" + msg + "```"


async def neko(to):
    await to.send('にゃーん')


async def members(members, to):
    members = filter(lambda member: not member.bot, members)
    member_names = map(lambda member: member.name, members)
    await to.send("**Member List:**\n" + code_block("\n".join(member_names)))


async def roles(roles, to):
    role_names = map(lambda role: role.name, roles)
    await to.send("**Role List:**\n" + code_block("\n".join(role_names)))
