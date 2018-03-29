# Ref:
# https://github.com/docker/docker-install/blob/master/install.sh

opt_ansible=0
opt_terraform=0
while [ $# -gt 0 ]; do
        case "$1" in
                --ansible)
                        opt_ansible="$2"
                        shift
                        ;;
                --terraform)
                        opt_terraform=1
                        ;;
                --*)
                        echo "Illegal option $1"
                        ;;
        esac
        shift $(( $# > 0 ? 1 : 0 ))
done

# !help test
case "$opt_ansible" in
    answers)
        echo "--ansible answers"
        ;;
    inventory)
        echo "--ansible inventory"
        ;;
esac

if [ $opt_terraform -eq 1 ]; then
    echo "--ansible enabled"
fi

# :!bash test_opts.sh --ansible inventory
