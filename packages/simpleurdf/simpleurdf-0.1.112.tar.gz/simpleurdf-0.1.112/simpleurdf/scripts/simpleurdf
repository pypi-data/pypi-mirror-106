#!/usr/bin/env bash
set -e
export BAGCLI_WORKDIR=$(cd $(dirname $0) && pwd)
. "$BAGCLI_WORKDIR/common"

cli_help() {
  cli_name=${0##*/}
  echo "
$cli_name
Brot and Games CLI
Version: $(cat $BAGCLI_WORKDIR/VERSION)
Usage: $cli_name [command]
Commands:
  create_pkg    create a description package ready to use
  *         Help
"
  exit 1
}

cli_log "Exporting config ..."
export $(cat "$BAGCLI_WORKDIR/config" | xargs)

case "$1" in
  create_pkg|c)
    "$BAGCLI_WORKDIR/commands/create_pkg" "$2" | tee -ia "$BAGCLI_WORKDIR/create_pkg_${2}.log"
    ;;
  *)
    cli_help
    ;;
esac