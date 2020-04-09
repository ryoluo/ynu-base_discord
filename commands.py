# coding: UTF-8

# target -> channel or user


async def neko(to):
    await to.send('にゃーん')


async def members(members, to):
    members = filter(lambda member: not member.bot, members)
    names = map(lambda member: member.name, members)
    await to.send("\n".join(names))
