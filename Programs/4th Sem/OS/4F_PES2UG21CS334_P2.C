#include <linux/sched/signal.h>

#include <linux/kernel.h>

#include <linux/module.h>

#include <linux/init.h>

#include <linux/sched.h>

MODULE_LICENSE("GPL");

char *str_s(int s)
{

    switch (s)
    {

    case TASK_RUNNING:

        return "RUNNING";

        break;

    case TASK_INTERRUPTIBLE:

        return "INTERRUPTIBLE";

        break;

    case TASK_UNINTERRUPTIBLE:

        return "UNINTERRUPTIBLE";

        break;

    case __TASK_STOPPED:

        return "STOPPED";

        break;

    case __TASK_TRACED:

        return "TRACED";

        break;

    case TASK_PARKED:

        return "PARKED";

        break;

    case TASK_DEAD:

        return "DEAD";

        break;

    case TASK_WAKEKILL:

        return "WAKEKILL";

        break;

    case TASK_WAKING:

        return "WAKING";

        break;

    case TASK_NOLOAD:

        return "NOLOAD";

        break;

    case TASK_NEW:

        return "NEW";

        break;

    case TASK_RTLOCK_WAIT:

        return "RTLOCK_WAIT";

        break;

    case TASK_KILLABLE:

        return "KILLABLE";

        break;

    case TASK_STOPPED:

        return "STOPPED";

        break;

    case TASK_IDLE:

        return "IDLE";

        break;

    case TASK_NORMAL:

        return "NORMAL";

        break;

    case TASK_REPORT:

        return "REPORT";

        break;

    default:

        return "NORMAL";

        break;
    }

    return "NORMAL";
}

void dfs(struct task_struct *task, int ind)
{

    struct task_struct *child;

    struct list_head *list;

    int i;

    for (i = 0; i < ind; i++)
    {

        printk(KERN_CONT "\t");
    }

    printk(KERN_CONT "|--Name: %s PID: %d State: %s\n", task->comm, task->pid, str_s(task->__state));

    list_for_each(list, &task->children)
    {

        child = list_entry(list, struct task_struct, sibling);

        dfs(child, ind + 1);
    }
}

static int dfs_in(void)
{

    printk(KERN_INFO "Listing all processes in DFS order:\n");

    dfs(&init_task, 0);

    return 0;
}

static void dfs_ex(void)
{

    printk(KERN_INFO "All processes listed in DFS order.");
}

module_init(dfs_in);

module_exit(dfs_ex);