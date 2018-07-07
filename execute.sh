#!/bin/sh

AUTHOR=""
VERSION=""

# don't have ? or * in file
while read -r file_line; do
  for word in $file_line; do
    case $word in

    esac
  done
done < "file_name.py.in"

_sub() ## USAGE: _sub STRING SUBSTRING REPLACEMENT
{      ## RESULT: stored in $_SUB
  _SUB=$1
  [ -n "$2" ] || return 1 ## nothing to search for: error
  s_srch=${2}  ## pattern to replace
  rep=$3       ## replacement string
  case $_SUB in
    *$s_srch*)    ## if pattern exists in the string
       sr1=${_SUB%%$s_srch*}  ## take the string preceding the first match
       sr2=${_SUB#*$s_srch}   ## and the string following the first match
       _SUB=$sr1$rep$sr2      ## and sandwich the replacement string between them
       ;;
    *) return 1 ;;   ## if the pattern does not exist, return an error code
  esac
}

sub() ## USAGE: sub STRING SUBSTRING REPLACEMENT
{     ## RESULT: printed to stdout
  _sub "$@"
  printf "%s\n" "$_SUB"
}
