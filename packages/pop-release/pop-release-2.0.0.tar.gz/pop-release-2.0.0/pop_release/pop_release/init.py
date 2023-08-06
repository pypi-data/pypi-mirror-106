from typing import List
import pathlib
import semantic_version


def __init__(hub):
    hub.pop.sub.add(dyne_name="idem")


def cli(hub):
    hub.pop.config.load(["pop_release", "idem", "acct"], cli="pop_release")

    hub.pop.loop.create()
    hub.pop.Loop.run_until_complete(
        hub.pop_release.init.run(
            root_path=pathlib.Path(hub.OPT.pop_release.root),
            version=hub.OPT.pop_release.ver,
            skip=hub.OPT.pop_release.skip,
            remote=hub.OPT.pop_release.remote,
            acct_file=hub.OPT.acct.acct_file,
            acct_key=hub.OPT.acct.acct_key,
            acct_profile=hub.OPT.acct.acct_profile,
        )
    )


async def run(
    hub,
    version,
    root_path: pathlib.Path,
    skip: List[str],
    remote: str,
    acct_file: str,
    acct_key: str,
    acct_profile: str,
):
    ctx = await hub.idem.ex.ctx(
        "exec.twine.",
        acct_file=acct_file,
        acct_key=acct_key,
        acct_profile=acct_profile,
    )
    if skip is None:
        skip = []
    if "semantic" not in skip:
        version = str(semantic_version.Version.coerce(str(version)))
    if "version" not in skip:
        hub.pop_release.version.set_ver(root_path, version)
        hub.pop_release.version.set_doc(root_path, version)
    if "test" not in skip:
        hub.pop_release.test.pytest(root_path)
    if "commit" not in skip:
        hub.pop_release.git.commit(root_path, version)
    if "tag" not in skip:
        hub.pop_release.git.tag(root_path, version)
    if "clean" not in skip:
        hub.pop_release.dist.clean(root_path)
    if "build" not in skip:
        hub.pop_release.dist.build(root_path)
    if "input" in skip:
        choice = "y"
    else:
        choice = input(
            f"Build for version {version} is complete, Push to git and pypi? [Y,n] "
        )
    if not choice or choice.lower().startswith("y"):
        if "release" not in skip:
            hub.log.info("Pushing to pypi")
            await hub.pop_release.twine.push(ctx, root_path)
        if "push" not in skip:
            hub.log.info("Pushing to git")
            hub.pop_release.git.push(root_path, remote)
    print("Success!")
