export interface Task {
  id: string;
  name: string;
  namespace: string;
}

export interface Todo {
  id: number;
  content: string;
}

export interface Meta {
  totalCount: number;
}
